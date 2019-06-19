from django.forms import ModelForm
from .models import MedicosData,PacientesData

class MedicosForm(ModelForm):
    class Meta:
        model = MedicosData
        fields = ['nome', 'sobrenome', 'nasc', 'CRM']

class PacientesForm(ModelForm):
    class Meta:
        model = PacientesData
        fields = ['nome', 'sobrenome', 'nasc', 'CPF']