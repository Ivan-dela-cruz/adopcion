from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import Mascota
from apps.solicitud.models import Solicitud
from django.core.files.storage import FileSystemStorage


def adoptadoss(request):

    mascotass = Mascota.objects.filter(estado='adoptado');
    mycontext = {
        'mascotas_data':mascotass
    }
    return render(request, 'mascota/adoptados.html', mycontext)

def index(request):

    mascotass = Mascota.objects.filter(estado='disponible');
    mycontext = {
        'mascotas_data':mascotass
    }
    return render(request, 'mascota/index.html', mycontext)

def add(request):
    mycontext={'mas':'hola mundo'}
    return render(request,'mascota/addMascota.html')

def create(request):
    print(request.POST)

    myfile = request.FILES['foto']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    #datos principales
    ci_pro = request.POST['cip']
    nombre = request.POST['nombre']
    raza = request.POST['raza']
    edad = request.POST['edad']
    descripcion = request.POST['descripcion']

    #descipcion fisica
    tamanio = request.POST['tamanio']
    sexo = request.POST['sexo']

    #salud
    alergia = request.POST['alergia']
    tratamiento = request.POST['tratamiento']
    enfermeda = request.POST['enfermedad']
    vacuna = request.POST['vacuna']

    #sociabilidad
    adultos = request.POST['adulto']
    ninios = request.POST['ninio']
    otros = request.POST['otro']

    #comportamiento
    carinioso = request.POST['carinioso']
    jugueton = request.POST['jugueton']
    tranquilo = request.POST['tranquilo']
    educado = request.POST['educado']

    #hitoria
    mihistoria = request.POST['historia']

    #estatus
    estado = 'disponible'

    mascota = Mascota(
        ci_pro = ci_pro,
        nombre = nombre,
        raza = raza,
        edad = edad,
        descripcion = descripcion,
        tamanio = tamanio,
        sexo = sexo,
        alergia = alergia,
        tratamiento = tratamiento,
        enfermeda = enfermeda ,
        vacuna = vacuna,
        adultos = adultos,
        ninios = ninios,
        otros = otros,
        carinioso = carinioso,
        jugueton = jugueton,
        tranquilo = tranquilo,
        educado = educado,
        mihistoria = mihistoria,
        estado = estado,
        foto = uploaded_file_url
    )
    mascota.save()
    return redirect('mascota:add')


def delete(request, id_mascota):
    mascota = Mascota.objects.get(pk=id_mascota)
    mascota.delete()
    return redirect('mascota:index')


def edit(request, id_mascota):
    mascota = Mascota.objects.get(pk=id_mascota)
    context = {
        'mascotas_data': mascota
    }
    return render(request, 'mascota/editMascota.html', context)


def update(request, id_mascota):
    mascota = Mascota.objects.get(pk=id_mascota)

    myfile = request.FILES['foto']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)

     #datos principales
    mascota.ci_pro = request.POST['cip']
    mascota.nombre = request.POST['nombre']
    mascota.raza = request.POST['raza']
    mascota.edad = request.POST['edad']
    mascota.descripcion = request.POST['descripcion']

    #descipcion fisica
    mascota.tamanio = request.POST['tamanio']
    mascota.sexo = request.POST['sexo']

    #salud
    mascota.alergia = request.POST['alergia']
    mascota.tratamiento = request.POST['tratamiento']
    mascota.enfermeda = request.POST['enfermedad']
    mascota.vacuna = request.POST['vacuna']

    #sociabilidad
    mascota.adultos = request.POST['adulto']
    mascota.ninios = request.POST['ninio']
    mascota.otros = request.POST['otro']

    #comportamiento
    mascota.carinioso = request.POST['carinioso']
    mascota.jugueton = request.POST['jugueton']
    mascota.tranquilo = request.POST['tranquilo']
    mascota.educado = request.POST['educado']

    #hitoria
    mascota.mihistoria = request.POST['historia']
    mascota.foto = uploaded_file_url

    mascota.save()
    return redirect('mascota:index')


def show(request, id_mascota):
    mascota = Mascota.objects.get(pk=id_mascota)
    context = {
        'mascotas': mascota
    }
    return render(request, 'mascota/adoptar.html', context)


def adoptarMascota(request, id_mascota):

    if request.user.is_authenticated:

        mascota = Mascota.objects.get(pk=id_mascota)

        solicitud = Solicitud(id_mascota = mascota,id_user=request.user)

        mascota.estado = 'adoptado'

        mascota.save()
        solicitud.save()
        return redirect('mascota:index')
