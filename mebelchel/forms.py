from .models import MebelchelOrders
from django.forms import ModelForm, TextInput


class MebelchelOrdersForm(ModelForm):
    class Meta:
        model = MebelchelOrders
        fields = ['type', 'name', 'phone']

        widgets = {
            'type': TextInput(attrs={
                'id': 'modal_type-input-input',
                'class': 'modal_type-input-input'
            }),
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


class MebelchelOrdersForm2(ModelForm):
    class Meta:
        model = MebelchelOrders
        fields = ['name', 'phone']

        widgets = {
            'name': TextInput(attrs={
                'id': 'order_name-input-input',
                'class': 'order_name-input-input',
                'placeholder': 'Александр'
            }),
            'phone': TextInput(attrs={
                'id': 'order_phone-input-input',
                'class': 'order_phone-input-input',
                'placeholder': '+7-912-123-45-67'
            })
        }
