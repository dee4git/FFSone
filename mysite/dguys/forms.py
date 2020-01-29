from django import forms

from .models import Dguy


class cvForm(forms.ModelForm):
    class Meta:
        model = Dguy
        fields = [
            'phone',
            'location',
            'cv',
            'photo'
        ]
