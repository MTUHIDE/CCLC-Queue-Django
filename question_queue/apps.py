from django.apps import AppConfig


class QuestionQueueConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "question_queue"

    def ready(self) -> None:
        from question_queue.util.group import ensure_group

        ensure_group("coach", [])
        ensure_group("student", [])
