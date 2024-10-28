from django.db import models
from django.forms import ValidationError

# Create your models here.
class Libros(models.Model):
    titulo = models.CharField(max_length=200,blank=False, null=False)
    autor = models.CharField(max_length=150, blank=False, null=False)
    valoracion = models.IntegerField(default=0, blank=False, null=False)
def __str__(self):
    return self.titulo

