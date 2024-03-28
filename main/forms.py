from django import forms
from django.forms import ModelForm, TextInput

from .models import SampleModel


class SampleModelForm(forms.ModelForm):
    class Meta:
        model = SampleModel
        fields = "__all__"

class myForms(forms.Form):
    name = forms.CharField(max_length=100)

def clean_mean(self):
    data = self.cleaned_data['name']
    if not data.isalfa():
        raise forms.ValidationError("Имя должно содержать только буквы.")
    return data

