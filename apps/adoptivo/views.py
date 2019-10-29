from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Adoptivo

def index(request):
    adoptivo = Adoptivo.objects.all();
    mycontext = {
        'adoptivo_data':adoptivo
    }
    return render(request, 'adoptivo/index.html', mycontext)

def add(request):
    pass

def create(request):
    pass

def delete(request, id_adoptivo):
    pass


def edit(request, id_adoptivo):
    pass

def update(request,id_adoptivo):
    pass

def show(request, id_adoptivo):
    pass
