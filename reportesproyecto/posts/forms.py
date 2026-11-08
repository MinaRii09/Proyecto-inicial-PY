from django import forms
from . import models

class CreatePost(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = [
            'title',
            'body',
            'banner',
            'categoria',
            'latitude',
            'longitude'
        ]

        labels = {
            'title': 'Título',
            'body': 'Descripción',
            'banner': 'Imágen',
        }

        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }