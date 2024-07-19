from django.urls import path
from .views import framework_view

urlpatterns = [
    path('', framework_view, name='framework'),
]

