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
            'body': forms.Textarea(attrs={
                'class': 'report-descripcion',
                'rows': 5,
            }),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if not title:
            raise forms.ValidationError(
                "El título no puede estar vacío."
            )

        return title

    def clean_body(self):
        body = self.cleaned_data['body'].strip()

        if not body:
            raise forms.ValidationError(
                "La descripción no puede estar vacía."
            )

        return body

    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')

        if not categoria:
            raise forms.ValidationError(
                "Debes seleccionar una categoría."
            )

        return categoria

    def clean(self):
        cleaned_data = super().clean()

        latitude = cleaned_data.get('latitude')
        longitude = cleaned_data.get('longitude')

        if latitude is None or longitude is None:
            raise forms.ValidationError(
                "Debes seleccionar una ubicación en el mapa."
            )

        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['categoria'].choices = [
            ('', 'Seleccione una categoría')
        ] + list(models.Post.CATEGORIAS)

        self.fields['latitude'].required = False
        self.fields['longitude'].required = False