from .models import Message
from django.forms import ModelForm, TextInput, Textarea


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тематика'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Контент'
            }),

            }