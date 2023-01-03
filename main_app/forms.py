from django.forms import ModelForm
from .models import Feeding
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
        widget = {
            'date': DateInput(),
        }