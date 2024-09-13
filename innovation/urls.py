from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('home.urls')),
    path('prisma/', include('prisma.urls')),
    path('necessity/', include('necessity_artifact.urls')),
    path('flujo_ml/',include('flujo_ml.urls')),
    path('flujo_blockchain/', include('flujo_blockchain.urls')),
]