from django import forms
from  django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistroForm(forms.Form):
    username = forms.CharField(label='Username',
                               max_length=100,
                               widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Contraseña',
                               max_length=100,
                               min_length=5,
                               widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña',
                                max_length=100,
                                min_length=5,
                                widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('El email ya existe')

        return email




