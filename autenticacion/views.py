from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class LoginView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
        return render(request, 'registro/registro.html', {'form': form})  # Agregado para manejar el caso de formulario no válido
