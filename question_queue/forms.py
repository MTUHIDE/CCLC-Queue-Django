from django import forms

from .models import CanvasCourse, Question, Reply

LANGUAGE_CHOICES = (
    ("1", "Java"),
    ("2", "C/C++"),
    ("3", "Javascript"),
    ("4", "Python"),
    ("5", "Rust"),
)


class NamedModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name}"


class QuestionForm(forms.Form):
    course = NamedModelChoiceField(required=False, queryset=CanvasCourse.objects.all())
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
