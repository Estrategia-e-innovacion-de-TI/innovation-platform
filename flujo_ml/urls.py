from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_flujo_view, name='inicio_flujo'),
    path('<str:paso>/', views.flujo_decision, name='flujo_decision'),
]