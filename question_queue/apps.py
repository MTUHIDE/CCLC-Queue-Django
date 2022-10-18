from django.apps import AppConfig


class QuestionQueueConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "question_queue"

    def ready(self) -> None:
        pass
