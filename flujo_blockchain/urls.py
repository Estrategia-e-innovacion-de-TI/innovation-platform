from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_flujo_blockchain_view, name='inicio_flujo_blockchain'),
    path('<str:paso>/', views.flujo_decision_blockchain, name='flujo_decision_blockchain'),
]