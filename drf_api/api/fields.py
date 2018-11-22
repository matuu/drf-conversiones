# coding: utf-8
from rest_framework import serializers

from core.utils import (
    lluvia_desde_api, lluvia_para_api,
    viento_desde_api, viento_para_api,
    temperatura_desde_api, temperatura_para_api)


class ConPerfilMixin(object):
    @property
    def perfil(self):
        return self.context["user"].perfil


class LluviaField(ConPerfilMixin, serializers.Field):
    """
    Campo para el manejo de los datos de lluvia
    """
    def to_representation(self, value):
        return lluvia_para_api(self.perfil, value)

    def to_internal_value(self, data):
        return lluvia_desde_api(self.perfil, data)


class VientoField(ConPerfilMixin, serializers.Field):
    """
    Campo para el manejo de los datos de viento
    """
    def to_representation(self, value):
        return viento_para_api(self.perfil, value)

    def to_internal_value(self, data):
        return viento_desde_api(self.perfil, data)


class TemperaturaField(ConPerfilMixin, serializers.Field):
    """
    Campo para el manejo de los datos de temperatura
    """
    def to_representation(self, value):
        return temperatura_para_api(self.perfil, value)

    def to_internal_value(self, data):
        return temperatura_desde_api(self.perfil, data)
