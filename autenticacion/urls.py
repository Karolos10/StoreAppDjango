from django.urls import path

from .views import LoginView, cerrar_sesion, logear

urlpatterns = [
    path('', LoginView.as_view(), name="autenticacion"),
    path('carrar_session',cerrar_sesion, name="cerrar_sesion"),
    path('login', logear, name="login"),
]
