from django import forms
from crispy_forms.helper import FormHelper
from .models import Computer, Instance

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        exclude = ("is_active","is_available",)

class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
        exclude = ("is_active","user",)