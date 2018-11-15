from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Perfil


@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if hasattr(instance, 'perfil'):
        print("creando perfil")
        Perfil.objects.create(usuario=instance)

