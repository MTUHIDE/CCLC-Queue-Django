from django import forms

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
    subject = forms.CharField(label='Subject:', max_length=100)
    question = forms.CharField(label='Question:', max_length=100)
    file = forms.FileField()
