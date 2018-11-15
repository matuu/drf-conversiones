from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import PerfilSerializer, RegistroSerializer
from core.models import Registro


class AuthView(APIView):
    """
    Clase base para vistas restringidas a usuarios identificados.
    """
    permission_classes = (IsAuthenticated, )


class WithContext(object):
    def get_serializer_context(self):
        """
        Inserta en el contexto del serializador, el request y el usuario.
        """
        return {
            'user': self.request.user,
            'request': self.request
        }


class PerfilUsuarioView(RetrieveAPIView, AuthView):
    """
    Devuelve el perfil del usuario.
    """
    http_method_names = ['get', ]
    serializer_class = PerfilSerializer

    def get_object(self):
        return self.request.user.perfil


class RegistroViewSet(WithContext, ModelViewSet, AuthView):
    http_method_names = ['get', 'post']
    serializer_class = RegistroSerializer

    def get_queryset(self):
        qs = Registro.objects.order_by('-creado_el')
        return qs
