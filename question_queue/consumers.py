import orjson
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.template.loader import render_to_string

from question_queue.models import QueueQuestion


class AsyncOrjsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    @classmethod
    async def decode_json(cls, text_data):
        return orjson.loads(text_data)

    @classmethod
    async def encode_json(cls, content):
        return orjson.dumps(content).decode("utf-8")


class CoachLiveQueueConsumer(AsyncOrjsonWebsocketConsumer):
    GROUP_NAME = "queue_group"

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(self.GROUP_NAME, self.channel_name)

        self.user = self.scope["user"]

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive_json(self, content):
        question_id = content["question_id"]
        action = content["action"]

        await self.process_queue_action(question_id, action)

        await self.channel_layer.group_send(self.GROUP_NAME, {"type": "html_message"})

    @database_sync_to_async
    def process_queue_action(self, question_id, action):
        question = QueueQuestion.objects.get(id=question_id)
        if action == "attending":
            question.attending = not question.attending
        elif action == "answered":
            question.answered_by = self.user
        elif action == "delete":
            question.hidden = True
        question.save()

    @database_sync_to_async
    def get_queue_questions(self):
        table_data = []
        for question in QueueQuestion.objects.filter(hidden=False):
            question_info = {
                "id": str(question.id),
                "name": question.asked_by.first_name,
                "class": question.course.name,
                "time": question.created_at,
                "message": question.message,
            }
            table_data.append(question_info)
        return table_data

    # Receive message from room group
    async def html_message(self, event):
        queue_questions = await self.get_queue_questions()
        # Send message to WebSocket
        await self.send_json(
            {
                "element": "#queue-table",
                "html": render_to_string(
                    "question_queue/question_table.html",
                    {"questions": queue_questions},
                ),
            }
        )
