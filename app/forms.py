#this folder we are creating in app
from django import forms
from app.models import *
class SchoolForm(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'