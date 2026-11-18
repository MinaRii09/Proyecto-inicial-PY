from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField(
        validators=[
            MinLengthValidator(10, message="El reporte debe tener una descripción del al menos 10 caracteres.")]
    )
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to="posts/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    latitude = models.FloatField()
    longitude = models.FloatField()

    CATEGORIAS = [
        ('incendio', '🔥 Incendio Patrimonial'),
        ('derrumbe', '🏚️ Derrumbe'),
        ('grafiti', '🎨 Grafiti o Vandalismo'),
        ('abandono', '🏠 Abandono de Inmueble'),
        ('demolicion', '🚧 Demolición'),
        ('monumento', '🗿 Daño a Monumento Histórico'),
        ('ascensor', '🛗 Daño a Ascensor Patrimonial'),
    ]

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
    )

    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('revision', 'En revisión'),
        ('resuelto', 'Resuelto'),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='pendiente',
    )

    NIVELES = [
        (1, 'Leve'),
        (2, 'Moderado'),
        (3, 'Importante'),
        (4, 'Grave'),
        (5, 'Crítico'),
    ]

    nivel = models.PositiveSmallIntegerField(
        choices=NIVELES,
        default=3,
        verbose_name='Nivel de importancia',
    )

    def __str__(self):
        return self.title
