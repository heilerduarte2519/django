from django.apps import AppConfig


class EjercicioeegConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ejercicioeeg'

class PacienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cognidroneeg.paciente'