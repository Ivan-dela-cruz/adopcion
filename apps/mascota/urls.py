from django.urls import path
from . import views

app_name = 'mascota'
urlpatterns = [

    path('index/', views.index, name="index"),
    path('adoptados/', views.adoptadoss, name="adoptados"),
    path('add/', views.add, name="add"),
    path('create/', views.create, name="create"),
    path('edit/<int:id_mascota>', views.edit, name="edit"),
    path('delete/<int:id_mascota>', views.delete, name="delete"),
    path('update/<int:id_mascota>', views.update, name="update"),
    path('show/<int:id_mascota>', views.show, name="show"),
    path('adoptar/<int:id_mascota>', views.adoptarMascota, name="adoptar"),
]
