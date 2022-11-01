from django import forms

from .models import Question, Reply

LANGUAGE_CHOICES = (
    ("1", "Java"),
    ("2", "C/C++"),
    ("3", "Javascript"),
    ("4", "Python"),
    ("5", "Rust"),
)


COURSE_CHOICES = (
    ("default", "﹀"),
    ("cs1121", "CS1121 - Intro to Programming 1"),
    ("cs1122", "CS1122 - Intro to Programming 2"),
    ("cs1131", "CS1131 - Accelerated Intro to Programming"),
    ("cs1142", "CS1142 - Programming at HW/SW Interface"),
    ("cs2311", "CS2311 - Discrete Structures"),
    ("cs2321", "CS2321 - Data Structures"),
    ("other", "other"),
)


class NamedModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name}"


class QuestionForm(forms.Form):
    course = forms.CharField(widget=forms.Select(choices=COURSE_CHOICES))
    question = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.Textarea(
            attrs={"class": "form-control", "style": "height: 100px"}
        ),
    )
    in_person = forms.BooleanField(
        label="In Person",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
    # language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
    # subject = forms.CharField(label="Subject:", max_length=100)
    # file = forms.FileField()

    class Meta:
        model = Question
        fields = ("course", "question", "in_person")


class FilterQueue(forms.Form):
    filter_queue = forms.CharField()


# Used by Coaches/Instructors
class AnswerForm(forms.Form):
    message = forms.CharField(
        label="Your Answer",
        required=True,
        widget=forms.Textarea(
            attrs={"class": "form-control", "style": "height: 100px"}
        ),
    )
    answer = forms.BooleanField(
        label="Mark as Answered",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )

    class Meta:
        model = Reply
        fields = ("answer", "message")


# Used by students (can't mark questions as answered)
class ReplyForm(forms.Form):
    message = forms.CharField(
        label="Your Answer",
        required=True,
        widget=forms.Textarea(
            attrs={"class": "form-control", "style": "height: 100px"}
        ),
    )

    class Meta:
        model = Reply
        fields = "message"
