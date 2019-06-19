from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class MedicosData(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    nasc = models.DateField()
    CRM = models.IntegerField(validators=[MaxValueValidator(99999)])

class PacientesData(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    nasc = models.DateField()
    CPF = models.IntegerField(validators=[MaxValueValidator(99999)])