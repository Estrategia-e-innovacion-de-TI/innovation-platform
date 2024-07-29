from django.urls import path
from .views import necessity_artifact_view

urlpatterns = [
    path('', necessity_artifact_view, name='necessity_artifact'),
]