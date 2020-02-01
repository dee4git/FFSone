from django import forms

from .models import Payment


class PayForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'refid',
        ]
