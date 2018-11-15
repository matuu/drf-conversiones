# coding: utf-8
from django.db import models
from django.conf import settings


class Perfil(models.Model):
    """
    Perfil asociado a un usuario. En él se configuran las preferencias del usuario.
    """
    LLUVIA_OPCIONES = (
        ('mm', 'mm'),
        ('in', 'inch'),
    )

    VIENTO_OPCIONES = (
        ('kph', 'km/h'),
        ('mph', 'mph')
    )

    TEMPERATURA_OPCIONES = (
        ('c', '°C'),
        ('f', '°F'),
    )

    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    temperatura_pref = models.CharField(max_length=1, choices=TEMPERATURA_OPCIONES, default='c')
    viento_pref = models.CharField(max_length=3, choices=VIENTO_OPCIONES, default='kph')
    lluvia_pref = models.CharField(max_length=2, choices=LLUVIA_OPCIONES, default='mm')

    def __str__(self):
        return f'perfil de {self.usuario}'


class Registro(models.Model):
    """
    Cada registro guardará la información climática del usuario,
    registrando quien lo registra, la hora y sus datos enviados
    """
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)

    temperatura = models.DecimalField(decimal_places=3, max_digits=5)
    viento = models.DecimalField(decimal_places=3, max_digits=6)
    lluvia = models.DecimalField(decimal_places=3, max_digits=5)

    def __str__(self):
        return f'datos del {self.creado_el} (@{self.usuario})'

    class Meta:
        verbose_name = 'registro'
        verbose_name_plural = 'registros'

