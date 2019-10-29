from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from  django.contrib.auth.models import User
from django.contrib import messages
from .form import UserRegistroForm


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse('historia:index'))

        else:
            messages.error(request, 'El usuario no existe')


    return render(request, 'usuario/login.html',{})

def logout_user(request):

    logout(request)

    return HttpResponseRedirect(reverse('usuario:login'))


def registro_user(request):

    form = UserRegistroForm()

    if request.method == 'POST':
        form = UserRegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username,email=email,password=password)
            messages.success(request,'Gracias por registrarse{}'.format(user.username))
            return HttpResponseRedirect(reverse('mascota:index'))
    else:
        form = UserRegistroForm()


    return render(request, 'usuario/registro.html', {'form':form})
