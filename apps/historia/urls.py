from django.urls import path
from . import views

app_name='historia'
urlpatterns = [
    path('index/', views.index, name="index"),
    path('addHistorias/', views.addHistoria, name="addHistorias"),
    path('likee/<int:id_historia>', views.megusta, name="likee"),
    path('mismemorias/', views.mishistorias, name="mismemorias"),
    path('crearhistorias/', views.crearHist, name="crearhistorias"),
]
