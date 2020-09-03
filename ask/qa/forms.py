from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(label="Заголовок: ", max_length=300)
    text = forms.CharField(label="Текст вопроса: ", widget=forms.Textarea, required=False)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(label="Ответить:", widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
