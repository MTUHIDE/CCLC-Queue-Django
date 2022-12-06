import asyncio

import orjson
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.db.models import F, Window
from django.db.models.functions import window
from django.template.loader import render_to_string

from question_queue.models import QueueQuestion, SupportedCourse


class AsyncOrjsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    @classmethod
    async def decode_json(cls, text_data):
        return orjson.loads(text_data)

    @classmethod
    async def encode_json(cls, content):
        return orjson.dumps(content).decode("utf-8")


class CoachLiveQueueConsumer(AsyncOrjsonWebsocketConsumer):
    COACH_GROUP_NAME = "coach_queue_group"
    STUDENT_GROUP_NAME = "student_queue_group"

    async def connect(self):
        stream = self.scope["url_route"]["kwargs"]["stream"]

        self.user = self.scope["user"]

        await self.accept()

        if stream == "coach":
            await self.channel_layer.group_add(self.COACH_GROUP_NAME, self.channel_name)
            await self.channel_layer.send(self.channel_name, {"type": "coach_message"})
        elif stream == "student":
            await self.channel_layer.group_add(
                self.STUDENT_GROUP_NAME, self.channel_name
            )
            await self.channel_layer.send(
                self.channel_name, {"type": "student_message"}
            )

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive_json(self, content):
        action = content["action"]
        args = content["args"]

        await self.process_queue_action(args, action)

        await asyncio.gather(
            self.channel_layer.group_send(
                self.COACH_GROUP_NAME, {"type": "coach_message"}
            ),
            self.channel_layer.group_send(
                self.STUDENT_GROUP_NAME, {"type": "student_message"}
            ),
        )

    @database_sync_to_async
    def process_queue_action(self, args, action):
        if action == "attending":
            question = QueueQuestion.objects.get(id=args["question_id"])
            question.attending = not question.attending
            question.save()
        elif action == "answered":
            question = QueueQuestion.objects.get(id=args["question_id"])
            question.answered_by = self.user
            question.save()
        elif action == "delete":
            question = QueueQuestion.objects.get(id=args["question_id"])
            question.hidden = True
            question.save()
        elif action == "create":
            question = QueueQuestion(
                course=SupportedCourse.objects.get(course_code=args["course"]),
                message=args["message"],
                asked_by=self.user,
            )
            question.save()

    @database_sync_to_async
    def get_queue_questions(self):
        table_data = []
        for question in QueueQuestion.objects.filter(
            hidden=False, answered_by__isnull=True
        ):
            attending = ""
            if question.attending:
                attending = "table-primary"
            question_info = {
                "id": str(question.id),
                "name": question.asked_by.first_name,
                "class": question.course.name,
                "time": question.created_at,
                "message": question.message,
                "attending": attending,
            }

            table_data.append(question_info)
        return table_data

    # Receive message from room group
    async def coach_message(self, event):
        queue_questions = await self.get_queue_questions()
        # Send message to WebSocket
        await self.send(
            render_to_string(
                "question_queue/question_table.html",
                {"questions": queue_questions},
            )
        )

    @database_sync_to_async
    def get_student_question(self):
        return (
            QueueQuestion.objects.filter(hidden=False, answered_by__isnull=True)
            .annotate(
                queue_position=Window(
                    expression=window.RowNumber(),
                    partition_by=[F("asked_by")],
                    order_by="created_at",
                )
            )
            .filter(asked_by=self.user)
            .first()
        )

    async def student_message(self, event):
        elements = []
        question = await self.get_student_question()
        elements.append(
            render_to_string(
                "question_queue/student/ask_question_btn.html",
                {"disabled": question is not None},
            ).rstrip()
        )
        index = -1
        if question:
            index = question.queue_position
        elements.append(
            render_to_string(
                "question_queue/student/queue_position.html",
                {"queue_position": index},
            ).rstrip()
        )
        await self.send("".join(elements))
