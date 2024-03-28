from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import ClassEntity

class ClassForm(forms.Form):
    classname = forms.CharField(max_length=255)
    details = forms.CharField(max_length=None)
    time = forms.DateTimeField()
    status = forms.BooleanField()