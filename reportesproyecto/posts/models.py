from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    # Google Maps location
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    CATEGORIAS = [
        ('incendio', 'Incendio Patrimonial'),
        ('derrumbe', 'Derrumbe'),
        ('grafiti', 'Grafiti o Vandalismo'),
        ('abandono', 'Abandono de Inmueble'),
        ('demolicion', 'Demolición'),
        ('monumento', 'Daño a Monumento Histórico'),
        ('ascensor', 'Daño a Ascensor Patrimonial'),
    ]

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        default='grafiti'
    )
    def __str__(self):
        return self.title