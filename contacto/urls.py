from django.urls import path

from . import views

urlpatterns = [
    path('', views.contacto, name="contacto"),
]

""" urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """