from django.shortcuts import render,redirect
from .models import Historia
from apps.mascota.models import Mascota
from apps.solicitud.models import Solicitud
from  django.contrib.auth.models import User

def index(request):

    historias = Historia.objects.all()
    if request.user.is_authenticated:
        user = User.objects.filter(email__exact='request.user.email')
        hist = Historia.objects.filter(id_adoptivo__exact=request.user.id)

    mycontext = {
        'historia_data':historias,
        'list_historia':hist
    }
    print(historias)
    return render(request, 'base/base.html', mycontext)


def megusta(request, id_historia):
    histori = Historia.objects.get(pk=id_historia)
    like = histori.like
    likes = like + 1

    histori.like = likes

    histori.save()
    return redirect('historia:index')

def addHistoria(request):

    mycontext={'mas':'hola mundo'}
    return render(request,'historia/crearHistoria.html')


def crearHist(request):
    if request.user.is_authenticated:
        solicitud = Solicitud.objects.filter(id_user__exact=request.user.id)
        for da in solicitud:
            print('valor : id_buscado')
            print(da.id_mascota.id_mascota)
            idd = da.id_mascota.id_mascota

        id_mascota = Mascota.objects.get(pk=idd)
        id_adoptivo = request.user
        titulo = request.POST['titulo']
        fecha = request.POST['fecha']
        historias = request.POST['historias']
        like = 0


        historia = Historia(
           id_mascota = id_mascota,
            id_adoptivo = id_adoptivo,
            historias = historias,
            fecha = fecha,
            like = like,
            titulo = titulo

        )
        historia.save()
        return redirect('historia:addHistorias')


def mishistorias(request):

    if request.user.is_authenticated:
        hist = Historia.objects.filter(id_adoptivo__exact=request.user.id)
        mascotas = Solicitud.objects.filter(id_user__exact=request.user.id)

        mycontext = {
            'historia_data':hist,
            'list_historia':hist,
            'lis_mas':mascotas
        }

        return render(request, 'usuario/mimascota.html', mycontext)
