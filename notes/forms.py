from django.shortcuts import redirect
from .models import Notes
from django.forms import ModelForm, TextInput, Textarea


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'note']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название заметки'
            }),
            'note': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Заметка'
            })
        }
