from django import forms

from user_data.models import Thesis


class ThesisForm(forms.ModelForm):

    class Meta:
        model = Thesis
        fields = ('cleaver',)
        widgets = {
            'cleaver': forms.Select(choices=Thesis.CHOICES)
        }
