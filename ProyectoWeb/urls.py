"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ProyectoWebApp/', include('ProyectoWebApp.urls')),
    path('ProyectoWebApp/servicios/', include('servicios.urls')),
    path('ProyectoWebApp/blog/', include('blog.urls')),
    path('ProyectoWebApp/contacto/', include('contacto.urls')),
    path('ProyectoWebApp/tienda/', include('tienda.urls')),
    path('ProyectoWebApp/carro/', include('carro.urls')),
    path('ProyectoWebApp/autenticacion/', include('autenticacion.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
