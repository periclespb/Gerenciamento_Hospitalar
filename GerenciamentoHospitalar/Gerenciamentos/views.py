from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def medicos(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "Gerenciamentos/medicos.html")
    #return HttpResponse(html)

def pacientes(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "Gerenciamentos/pacientes.html")
    #return HttpResponse(html)

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

