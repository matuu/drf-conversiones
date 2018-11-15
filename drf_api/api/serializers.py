# coding: utf-8
from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed

from core.models import Perfil, Registro


class PerfilSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.CharField(source='usuario.username', read_only=True)
    nombre_pila = serializers.CharField(source='usuario.first_name', read_only=True)
    apellido = serializers.CharField(source='usuario.last_name', read_only=True)

    temperatura_pref = serializers.CharField(source='get_temperatura_pref_display')
    lluvia_pref = serializers.CharField(source='get_lluvia_pref_display')
    viento_pref = serializers.CharField(source='get_viento_pref_display')

    class Meta:
        model = Perfil
        fields = (
            'nombre_usuario', 'nombre_pila', 'apellido',
            'temperatura_pref', 'lluvia_pref', 'viento_pref'
        )


class RegistroSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.CharField(read_only=True, source="usuario.username")

    class Meta:
        model = Registro
        fields = ('nombre_usuario', 'temperatura', 'viento', 'lluvia')

    def create(self, validated_data):
        registro = Registro(**validated_data)
        _usuario = self.context["user"]
        registro.usuario = _usuario
        registro.save()
        return registro

    def update(self, instance, validated_data):
        raise MethodNotAllowed("No se puede actualizar los registros")
