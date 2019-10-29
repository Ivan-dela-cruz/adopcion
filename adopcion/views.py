from django.shortcuts import render
from django.views.generic import View


def Home(request):
    contexto = {}
    return render(request, 'base/base.html', contexto)
