from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, ModelForm, PasswordInput, CharField


class UserLoginForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = CharField(widget=TextInput(attrs={
                'name': 'username',
                'value': 'Логин',
                'class': 'input username',
                'onfocus': 'this.value=""'
            }))
    password = CharField(widget=PasswordInput(attrs={
                'name': 'password',
                'value': 'Пароль',
                'class': 'input password',
                'onfocus': 'this.value=""'
            }))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)


class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={
                'name': 'username',
                'value': 'Логин',
                'class': 'input username',
                'onfocus': 'this.value=""'
            }),
            'password': PasswordInput(attrs={
                'name': 'password',
                'value': 'Пароль',
                'class': 'input password',
                'onfocus': 'this.value=""'
            })
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
