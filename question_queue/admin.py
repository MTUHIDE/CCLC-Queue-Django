from django.contrib import admin

from question_queue.models import (
    Assignment,
    CanvasCourse,
    EnrolledIn,
    Question,
    QueueQuestion,
    Reply,
    SupportedCourse,
    User,
)


@admin.register(CanvasCourse)
class CanvasCourseAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    pass


@admin.register(EnrolledIn)
class EnrolledInAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"


@admin.register(QueueQuestion)
class QueueQuestionAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"


@admin.register(SupportedCourse)
class SupportedCourseAdmin(admin.ModelAdmin):
    pass
