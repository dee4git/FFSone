from django import forms

from .models import Enrolment , Rating


class EnrolmentForm(forms.ModelForm):
    class Meta:
        model = Enrolment
        fields = [
            'phone',
            'address',
            'duration',
                    ]


class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
            'rating',
            'comment',

                    ]
