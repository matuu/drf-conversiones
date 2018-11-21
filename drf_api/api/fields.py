# coding: utf-8
from rest_framework import serializers

from core.utils import (
    lluvia_desde_api, lluvia_para_api,
    viento_desde_api, viento_para_api,
    temperatura_desde_api, temperatura_para_api)


class LluviaField(serializers.Field):
    """
    Campo para el manejo de los datos de lluvia
    """
    def to_representation(self, value):
        perfil = self.context["user"].perfil
        return lluvia_para_api(perfil, value)

    def to_internal_value(self, data):
        perfil = self.context["user"].perfil
        return lluvia_desde_api(perfil, data)


class VientoField(serializers.Field):
    """
    Campo para el manejo de los datos de viento
    """
    def to_representation(self, value):
        perfil = self.context["user"].perfil
        return viento_para_api(perfil, value)

    def to_internal_value(self, data):
        perfil = self.context["user"].perfil
        return viento_desde_api(perfil, data)


class TemperaturaField(serializers.Field):
    """
    Campo para el manejo de los datos de temperatura
    """
    def to_representation(self, value):
        perfil = self.context["user"].perfil
        return temperatura_para_api(perfil, value)

    def to_internal_value(self, data):
        perfil = self.context["user"].perfil
        return temperatura_desde_api(perfil, data)
