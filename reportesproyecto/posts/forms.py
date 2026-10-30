from django import forms
from . import models

class CreatePost(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = [
            'title',
            'body',
            'slug',
            'banner',
            'categoria',
            'latitude',
            'longitude'
        ]

        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }