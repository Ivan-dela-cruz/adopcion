from django.urls import path
from . import views

app_name='adoptivo'
urlpatterns = [
    path('index/', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('create/', views.create, name="create"),
    path('edit/<int:id_adoptivo>', views.edit, name="edit"),
    path('delete/<int:id_adoptivo>', views.delete, name="delete"),
    path('update/<int:id_adoptivo>', views.update, name="update"),
    path('show/<int:id_adoptivo>', views.show, name="show"),

]
