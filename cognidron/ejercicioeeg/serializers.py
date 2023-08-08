from rest_framework import serializers
from ejercicioeeg.models import Ejercicioeeg, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from ejercicioeeg.models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['idPaciente', 'nombre', 'ape_paterno', 'ape_materno', 'genero', 'fecha_nacimiento','borradoLogico']
        
class UserSerializer(serializers.ModelSerializer):
    ejercicioeeg = serializers.PrimaryKeyRelatedField(many=True, queryset=Ejercicioeeg.objects.all())
    ejercicioeeg = serializers.HyperlinkedRelatedField(many=True, view_name='ejercicioeeg-detail', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'ejercicioeeg']

class CustomEjercicioeegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicioeeg
        fields = ['idEjercicioeeg', 'idEjercicios', 'idPaciente', 'F3BethaH', 'F3BethaL', 'F3Theta','F3Gamma','F3Alpha','F4BethaH','F4BethaL','F4Theta','F4Gamma','F4Alpha','eliminado','owner','calculado1','calculado2','calculado3','fechaRegistro','fechaint','fechastring','slider']
        
class EjercicioeegSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Ejercicioeeg
        fields = ['idEjercicioeeg', 'idEjercicios', 'idPaciente', 'F3BethaH', 'F3BethaL', 'F3Theta','F3Gamma','F3Alpha','F4BethaH','F4BethaL','F4Theta','F4Gamma','F4Alpha','eliminado','owner','calculado1','calculado2','calculado3','fechaRegistro','fechaint','fechastring','slider']
        owner = serializers.ReadOnlyField(source='auth.User')

    def create(self, validated_data):
        return Ejercicioeeg.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idEjercicios = validated_data.get('idEjercicios', instance.idEjercicios)
        instance.idPaciente = validated_data.get('idPaciente', instance.idPaciente)

        instance.F3BethaH = validated_data.get('F3BethaH', instance.F3BethaH)
        instance.F3BethaL = validated_data.get('F3BethaL', instance.F3BethaL)
        instance.F3Theta = validated_data.get('F3Theta', instance.F3Theta)
        instance.F3Gamma = validated_data.get('F3Gamma', instance.F3Gamma)
        instance.F3Alpha = validated_data.get('F3Alpha', instance.F3Alpha)

        instance.F4BethaH = validated_data.get('F4BethaH', instance.F4BethaH)
        instance.F4BethaL = validated_data.get('F4BethaL', instance.F4BethaL)
        instance.F4Theta = validated_data.get('F4Theta', instance.F4Theta)
        instance.F4Gamma = validated_data.get('F4Gamma', instance.F4Gamma)
        instance.F4Alpha = validated_data.get('F4Alpha', instance.F4Alpha)

        #instance.fechaActividad = validated_data.get('fechaActividad', instance.fechaActividad)
        #instance.f3BetaL = validated_data.get('f3BetaL', instance.f3BetaL)
        #instance.f3BetaH = validated_data.get('f3BetaH', instance.f3BetaH)
        instance.calculado1 = validated_data.get('calculado1', instance.calculado1)
        instance.calculado2 = validated_data.get('calculado2', instance.calculado2)
        instance.calculado3 = validated_data.get('calculado3', instance.calculado3)
        instance.eliminado = validated_data.get('eliminado', instance.eliminado)
        instance.fechaint = validated_data.get('fechaint', instance.fechaint)
        instance.fechastring = validated_data.get('fechastring', instance.fechastring)
        instance.slider = validated_data.get('slider', instance.slider)
        instance.save()
        return instance