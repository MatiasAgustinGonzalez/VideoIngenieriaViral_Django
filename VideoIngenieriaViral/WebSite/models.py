from django.db import models

class TarjetaInicio(models.Model):
  titulo = models.CharField(max_length=100)
  cuerpo = models.CharField(max_length=600)

  def __str__(self):
    return f"Se cargó el texto {self.titulo}"
