"""GerenciamentoHospitalar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Gerenciamentos.views import medicos,pacientes,medicamentos,diagnostico,equipamentos,login,relatorioPaciente,fichaMedico,atestado,horaMedicacao,novoMedico,update,delete,novoPacientes,updatePacientes,deletePacientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medicos/',medicos),
    path('pacientes/',pacientes),
    path('medicamentos/', medicamentos),
    path('equipamentos/', equipamentos),
    path('diagnosticos/', diagnostico),
    path('login/', login),
    path('relatorioPaciente/', relatorioPaciente),
    path('fichaMedico/', fichaMedico),
    path('atestado/', atestado),
    path('horaMedicacao/', horaMedicacao),
    path('adicionarmedico/', novoMedico),
    path('update/<int:pk>/', update),
    path('delete/<int:pk>/', delete),
    path('adicionarpacientes/', novoPacientes),
    path('updatepacientes/<int:pk>/', updatePacientes),
    path('deletepacientes/<int:pk>/', deletePacientes),
]
