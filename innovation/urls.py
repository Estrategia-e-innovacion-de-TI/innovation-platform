from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prisma/', include('prisma.urls')),
    path('necessity/', include('necessity_artifact.urls')),
]
