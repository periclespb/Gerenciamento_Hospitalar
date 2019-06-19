from django.shortcuts import render
from .models import MedicosData,PacientesData
from .form import MedicosForm,PacientesForm

# Create your views here.
from django.http import HttpResponse
import datetime

def medicos(request):
    data = {}
    data['medicosData'] = MedicosData.objects.all()
    return render(request, "Gerenciamentos/medicos.html", data)

def novoMedico(request):
    data = {}
    form = MedicosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return medicos(request)

    data['form'] = form
    return render(request, "Gerenciamentos/adicionarmedicos.html", data)

def update(request, pk):
    data = {}
    medicos_ = MedicosData.objects.get(pk=pk)
    form = MedicosForm(request.POST or None, instance=medicos_)

    if form.is_valid():
        form.save()
        return medicos(request)

    data['form'] = form
    data['medicos_'] = medicos_
    return render(request, "Gerenciamentos/adicionarmedicos.html", data)

def pacientes(request):
    data = {}
    data['pacientesData'] = PacientesData.objects.all()
    return render(request, "Gerenciamentos/pacientes.html", data)

def novoPacientes(request):
    data = {}
    form = PacientesForm(request.POST or None)

    if form.is_valid():
        form.save()
        return pacientes(request)

    data['form'] = form
    return render(request, "Gerenciamentos/adicionarpacientes.html", data)

def updatePacientes(request, pk):
    data = {}
    pacientes_ = PacientesData.objects.get(pk=pk)
    form = PacientesForm(request.POST or None, instance=pacientes_)

    if form.is_valid():
        form.save()
        return pacientes(request)

    data['form'] = form
    data['pacientes_'] = pacientes_
    return render(request, "Gerenciamentos/adicionarpacientes.html", data)



def diagnostico(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "Gerenciamentos/diagnostico.html")
    #return HttpResponse(html)

def equipamentos(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "Gerenciamentos/equipamentos.html")
    #return HttpResponse(html)


def medicamentos(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "Gerenciamentos/medicamentos.html")
    #return HttpResponse(html)

def login(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "Gerenciamentos/login.html")
    #return HttpResponse(html)

def relatorioPaciente(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "Gerenciamentos/relatorioPaciente.html")
    #return HttpResponse(html)

def fichaMedico(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "Gerenciamentos/fichaMedico.html")
    #return HttpResponse(html)

def atestado(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "Gerenciamentos/atestado.html")
    #return HttpResponse(html)

def horaMedicacao(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "Gerenciamentos/horaMedicacao.html")
    #return HttpResponse(html)

def delete(request, pk):
    data = {}
    medicos_ = MedicosData.objects.get(pk=pk)
    medicos_.delete()
    return medicos(request)

def deletePacientes(request, pk):
    data = {}
    pacientes_ = PacientesData.objects.get(pk=pk)
    pacientes_.delete()
    return pacientes(request)
