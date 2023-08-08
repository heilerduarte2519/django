from pyexpat import model
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Ejercicioeeg(models.Model):
    idEjercicioeeg = models.BigAutoField(primary_key=True)
    idEjercicios = models.IntegerField(blank=False,null=False)
    idPaciente = models.IntegerField(blank=False,null=False)
    #fechaRegistro = models.DateField(auto_now_add=True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    #sensor = models.CharField(blank=False,null=False,max_length=4,default="sin")
    #banda = models.CharField(blank=False,null=False,max_length=10,default="sin")
    #fechaActividad=models.DateTimeField(auto_now_add=False,editable=True)
    F3BethaH=models.FloatField(null=False, blank=False, default=0)
    F3BethaL=models.FloatField(null=False, blank=False, default=0)
    F3Theta=models.FloatField(null=False, blank=False, default=0)
    F3Gamma=models.FloatField(null=False, blank=False, default=0)
    F3Alpha=models.FloatField(null=False, blank=False, default=0)

    F4BethaH=models.FloatField(null=False, blank=False, default=0)
    F4BethaL=models.FloatField(null=False, blank=False, default=0)
    F4Theta=models.FloatField(null=False, blank=False, default=0)
    F4Gamma=models.FloatField(null=False, blank=False, default=0)
    F4Alpha=models.FloatField(null=False, blank=False, default=0)
    
    calculado1=models.FloatField(null=False, blank=False, default=0)
    calculado2=models.FloatField(null=False, blank=False, default=0)
    calculado3=models.FloatField(null=False, blank=False, default=0)
    eliminado = models.BooleanField(default=False)
    fechaint = models.CharField(blank=False,null=False,max_length=8)
    fechastring = models.CharField(blank=False,null=False,max_length=50)
    slider=models.FloatField(null=False, blank=False, default=0)
    #fechaRegistro=models.DateTimeField(null=True, blank=True,auto_now_add=False,editable=True)
    owner = models.ForeignKey('auth.User', related_name='ejercicioeeg', on_delete=models.CASCADE)

    class Meta:
        ordering = ['fechaRegistro']
    

class Paciente(models.Model):
    idPaciente = models.BigAutoField(primary_key=True)
    nombre = models.CharField(null=False,max_length=45)
    ape_paterno = models.CharField(null=False,max_length=45)
    ape_materno = models.CharField(null=False,max_length=45)
    genero = models.CharField(null=False,max_length=45)
    fecha_nacimiento= models.CharField(null=False,max_length=45)
    borradoLogico= models.CharField(null=False,max_length=45)
    class Meta:
        db_table = 'paciente'
        ordering = ['nombre']
        