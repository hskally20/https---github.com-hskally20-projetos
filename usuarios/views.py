from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .form import UsuarioForm
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect 
from django.db import migrations
from django.contrib.auth.models import Group

def logout_view(request): 
    auth.logout(request) 
    return redirect('')

class home(View):
    def get(self, request):
       return HttpResponse('Class based view')

    def post(self,request):
      return HttpResponse('Class based view')
class UsuarioCreate(CreateView):
    form_class = UsuarioForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        # Verifica se o grupo 'Paciente' existe
        grupo = get_object_or_404(Group, name='Paciente')
        # Chama o método form_valid da superclasse para salvar o formulário
        response = super().form_valid(form)
        # Adiciona o usuário ao grupo
        self.object.groups.add(grupo)
        self.object.save()
        return response

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['Titulo'] = 'Registra Novo Usuario '
        return context
