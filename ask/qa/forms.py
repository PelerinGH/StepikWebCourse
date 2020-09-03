from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(label="Заголовок: ", max_length=300)
    text = forms.CharField(label="Текст вопроса: ", widget=forms.Textarea, required=False)

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(label="Ответить:", widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('A user with the same username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A user with the same email already exists')
        return email

    def save(self):
        user = User(**self.cleaned_data)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        data = self.cleaned_data['username']
        if not data:
            raise forms.ValidationError("Please enter username")
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        if not data:
            raise forms.ValidationError("Please enter password")
        return data
