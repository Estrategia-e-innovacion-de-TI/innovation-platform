from django.urls import path
from . import views

urlpatterns = [
    path('use_cases/', views.use_cases, name='use_cases'),
    path('business_value/', views.business_value, name='business_value'),
    path('feasibility_value/', views.feasibility_value, name='feasibility_value'),
    path('califications/', views.califications, name='califications'),
    path('artifacts/', views.artefacto_view, name='artifacts'),
]