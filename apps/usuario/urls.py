from django.urls import path
from . import views

app_name = 'usuario'
urlpatterns = [

    path('login/', views.login_user, name="login"),
    path('registro/', views.registro_user, name="registro"),
    path('logout/', views.logout_user, name="logout"),
]
