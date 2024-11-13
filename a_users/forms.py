from django.forms import ModelForm
from django import forms
from .models import *


class ProfileFrom(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        labels = {
            'realname': 'Name',
        }

        widgets = {
            'image': forms.FileInput(),
            'bio': forms.Textarea(attrs={'rows': 3})
        }


