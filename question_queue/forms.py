from django import forms
from .models import Reply

LANGUAGE_CHOICES = (
    ("1", "Java"),
    ("2", "C/C++"),
    ("3", "Javascript"),
    ("4", "Python"),
    ("5", "Rust"),
)


class QuestionForm(forms.Form):
    assignment = forms.ChoiceField()
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
    subject = forms.CharField(label="Subject:", max_length=100)
    question = forms.CharField(label="Question:", max_length=100)
    file = forms.FileField()


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
