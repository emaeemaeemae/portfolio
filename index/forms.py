from .models import CallRequests
from django.forms import ModelForm, TextInput


class CallRequestsForm(ModelForm):
    class Meta:
        model = CallRequests
        fields = ['name', 'phone']

        widgets = {
            'name': TextInput(attrs={
                'id': 'modal_name-input-input',
                'class': 'modal_name-input-input',
                'placeholder': 'Александр'
            }),
            'phone': TextInput(attrs={
                'id': 'modal_phone-input-input',
                'class': 'modal_phone-input-input',
                'placeholder': '+7-912-123-45-67'
            })
        }
