from django.urls import path
from . import views

urlpatterns = [
    path('', views.use_cases, name='prisma'),
    path('business_value/', views.business_value, name='business_value'),
    path('feasibility_value/', views.feasibility_value, name='feasibility_value'),
    path('califications/', views.califications, name='califications'),
    path('artifact/', views.artefacto_view, name='artifact'),
    path('diagram/', views.prisma_diagram, name='diagram'),
] 