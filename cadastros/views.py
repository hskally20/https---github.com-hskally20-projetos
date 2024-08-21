from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from .models import Hospital, Medico ,Paciente,Cronograma ,Consulta,Comentario, Triagem
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render


 # <=============== usuarios ==============>

class HospitalCreate(GroupRequiredMixin, CreateView):
    group_required = u"Admin"
    login_url = reverse_lazy('login')
    model = Hospital
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-hospital')
    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['Titulo'] = 'Cadastro de Hospitais '
     
      return context
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class MedicoCreate(GroupRequiredMixin, CreateView):
    group_required = u"Admin"
    login_url = reverse_lazy('login')
    model = Medico
    fields = ['numero', 'nome', 'cpf', 'especificacao', 'hospital']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-medico')
    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['Titulo'] = 'Cadastro de Medicos '
      return context
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class PacienteCreate(GroupRequiredMixin, CreateView):
    group_required = u'Paciente' 
    login_url = reverse_lazy('login')
    model = Paciente
    fields = ['telefone', 'nome', 'numero_sus','hospital','doença_cronica','sintomas','idade']
    template_name = 'form.html'
    success_url = reverse_lazy('Listar-paciente')
    def form_valid(self, form):
        if (form.instance.idade < 59  ): 
           form.instance.descricao ='comun'
           if ( form.instance.doença_cronica =='' or form.instance.doença_cronica is None ): 
              form.instance.descricao ='comun'
           else:
              form.instance.descricao ='preferencial'
        else:
          form.instance.descricao = 'preferencial'
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
       
    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['Titulo'] = 'Cadastro de Pacientes '
      context['conteudo'] = 'se nao tem doença crônica nao prenchar o campo abaixo !'
      return context

class TriagemCreate(GroupRequiredMixin, CreateView):
    group_required = u'Medico' 
    login_url = reverse_lazy('login')
    model = Triagem
    fields = ['data','horario', 'pressao', 'hospital', 'medico' , 'paciente']
    template_name = 'form.html'
    success_url = reverse_lazy('Listar-triagem') 
    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['Titulo'] = 'Cadastro de triagens'
      context['conteudo'] = 'prenchar todos os campos'
      return context
   



# Update
class HospitalUpdate(GroupRequiredMixin, UpdateView):
    group_required = u"Admin"
    login_url = reverse_lazy('login')
    model = Hospital
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-hospital')
    def get_object(self, query=None):
      self.object = Hospital.objects.get(pk = self.kwargs['pk'], usuario =
      self.request.user)
      return self.object

 

class MedicoUpdate(GroupRequiredMixin ,UpdateView):
    group_required = u"Admin"
    model = Medico
    fields = ['numero', 'nome', 'cpf', 'especificacao', 'hospital']
    template_name = 'form.html'
    success_url = reverse_lazy('inicio')
    def get_object(self, query=None):
      self.object = Medico.objects.get(pk = self.kwargs['pk'], usuario =
      self.request.user)
      return self.object


class PacienteUpdate(GroupRequiredMixin, UpdateView):
    group_required = u"Paciente"
    model = Paciente
    fields =['telefone', 'nome', 'numero_sus','hospital','doença_cronica','sintomas','idade']
    template_name = 'form.html'
    success_url = reverse_lazy('Listar-paciente')
    def get_object(self, query=None):
      self.object = Paciente.objects.get(pk = self.kwargs['pk'], usuario =
      self.request.user)
      return self.object
    def form_valid(self, form):
        if (form.instance.idade < 59  ): 
           form.instance.descricao ='comun'
           if ( form.instance.doença_cronica =='' or form.instance.doença_cronica is None ): 
              form.instance.descricao ='comun'
           else:
              form.instance.descricao ='preferencial'
        else:
          form.instance.descricao = 'preferencial'
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class TriagemUpdate(GroupRequiredMixin, UpdateView):
    group_required = u"Paciente"
    model = Triagem
    fields = ['paciente', 'data', 'medico', 'hospital', 'horario', 'pressao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-triagem')
    def get_object(self, query=None):
      self.object = Triagem.objects.get(pk = self.kwargs ['pk'], usuario =
      self.request.user)
      return self.object

    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['Titulo'] = 'Cadastro de triagens'
      context['conteudo'] = 'prenchar todos os campos'
      return context

# Delete
class HospitalDelete(GroupRequiredMixin, DeleteView):
    group_required = u"Admin"
    login_url = reverse_lazy('login')
    model = Hospital
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-hospital')
    def get_object(self, query=None):
      self.object = Hospital.objects.get(pk = self.kwargs ['pk'], usuario =
      self.request.user)
      return self.object

class  MedicoDelete(GroupRequiredMixin,DeleteView):
    group_required = u"Admin"
    model =  Medico
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('inicio')
    def get_object(self, query=None):
      self.object = Medico.objects.get(pk = self.kwargs ['pk'], usuario =
      self.request.user)
      return self.object


class  Pacientedelete(GroupRequiredMixin,DeleteView):
    group_required = u'Paciente'
    model =  Paciente
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('Listar-paciente')
    def get_object(self, query=None):
      self.object = Paciente.objects.get(pk = self.kwargs ['pk'], usuario =
      self.request.user)
      return self.object

class TriagemDelete(GroupRequiredMixin, DeleteView):
    group_required = u'Medico' 
    login_url = reverse_lazy('login')
    model = Triagem
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('Listar-triagem')
    def get_object(self, query=None):
      self.object = Triagem.objects.get(pk = self.kwargs ['pk'], usuario =
      self.request.user)
      return self.object
       
    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['Titulo'] = 'Cadastro de triagens'
      context['conteudo'] = 'prenchar todos os campos'
      return context

# List
class HospitalList(GroupRequiredMixin, ListView):
    group_required = u'Admin'
    login_url = reverse_lazy('login')
    model = Hospital
    template_name = 'listas/hospital.html'
    paginate_by = 5
    def get_queryset(self):
       nome = self.request.GET.get('nome')
       if nome:
           hospital = Hospital.objects.filter(nome__icontains = nome)
       else:
         hospital= Hospital.objects.all()
       return hospital
    
class MedicoList(GroupRequiredMixin, ListView):
    group_required = u'Medico'
    login_url = reverse_lazy('login')
    model = Medico
    template_name = 'listas/medico.html'
    paginate_by = 5
    def get_queryset(self):
       nome = self.request.GET.get('nome')
       if nome:
        medico = Medico.objects.filter(nome__icontains = nome)
       else:
         medico = Medico.objects.all()
       return medico
class PacienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Paciente
    template_name = 'listas/Paciente.html'
    paginate_by = 5
    def get_queryset(self):
       nome = self.request.GET.get('nome')
       if nome:
         paciente = Paciente.objects.filter(nome__icontains = nome)
       else:
         paciente = Paciente.objects.all()
       return paciente

class TriagemList(GroupRequiredMixin, ListView):
    group_required = u'Medico'
    login_url = reverse_lazy('login')
    model = Triagem
    template_name = 'listas/triagem.html'
    paginate_by = 5
    def get_queryset(self):
       nome = self.request.GET.get('nome')
       if nome:
         paciente = Triagem.objects.filter(nome__icontains = nome)
       else:
         paciente = Triagem.objects.all()
       return paciente
     

# <================   funçoes do site   ==================>

class CronogramaCreate(GroupRequiredMixin,CreateView):
    group_required = u"Medico"
    login_url = reverse_lazy('login')
    model = Cronograma
    fields = ['nome', 'data','medico','hospital','horario']
    template_name = 'form.html'
    success_url = reverse_lazy('Listar-cronograma')
    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['Titulo'] = 'Cadastro de Cronogramas '
      return context
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
class CronogramaDelete(GroupRequiredMixin,DeleteView):
    group_required = u"Medico"
    model = Cronograma
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('Listar-cronograma')
    def get_object(self, query=None):
      self.object = Cronograma.objects.get(pk = self.kwargs ['pk'], usuario =
      self.request.user)
      return self.object
    
class CronogramaUpdate( GroupRequiredMixin,UpdateView):
    group_required = u"Medico"
    login_url = reverse_lazy('login')
    model = Cronograma
    fields = ['paciente',' data','medico','hospital',' horario', 'pressao']
    template_name = 'form.html'
    success_url = reverse_lazy('Listar-cronograma')
    def get_object(self, query=None):
      self.object = Cronograma.objects.get(pk = self.kwargs ['pk'], usuario =
      self.request.user)
      return self.object
    

class CronogramaList(ListView):
    model = Cronograma
    template_name = 'listas/cronograma.html'
    paginate_by = 5
    def get_queryset(self):
      nome = self.request.GET.get('nome')
      if nome:
         cronograma = Cronograma.objects.filter(nome__icontains = nome)
      else:
         cronograma = Cronograma.objects.all()
      return cronograma

class ConsultaCreate(CreateView):
    login_url = reverse_lazy('login')
    model = Consulta
    fields = ['paciente', 'data','medico','hospital','horario']
    template_name = 'form.html'
    success_url = reverse_lazy('Listar-consulta')
    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['Titulo'] = ' agendar Consulta '
      return context
    def form_valid(self, form):
      if ( form.instance.status =='None' or form.instance.status is None ):        
           form.instance.status = 'pendente'
       
      else:
          form.instance.status = 'pendente'
      form.instance.usuario = self.request.user
      url = super().form_valid(form)
      return url
class ConsultaDelete(DeleteView):
    model = Consulta
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('Listar-consulta')
    def get_object(self, query=None):
      self.object = Consulta.objects.get(pk = self.kwargs ['pk'], usuario =
      self.request.user)
      return self.object
    
class ConsultaUpdate( UpdateView):
    model = Consulta
    fields = ['paciente', 'data','medico','hospital','horario']
    template_name = 'form.html'
    success_url = reverse_lazy('Listar-consulta')
    def get_object(self, query=None):
      self.object = Consulta.objects.get(pk = self.kwargs ['pk'], usuario =
      self.request.user)
      return self.object
    def form_valid(self, form):
      if ( form.instance.status =='None' or form.instance.status is None ):        
           form.instance.status = 'pendente'
      else:
          form.instance.status = 'pendente'
      form.instance.usuario = self.request.user
      url = super().form_valid(form)
      return url

class Consulta2Update( UpdateView):
    model = Consulta
    fields = ['status']
    template_name = 'form.html'
    success_url = reverse_lazy('Listar-consulta')
      
    

class ConsultaList(ListView):
    login_url = reverse_lazy('login')
    model = Consulta
    template_name = 'listas/consulta.html'
    paginate_by = 5
    def get_queryset(self):
      consultas = Consulta.objects.all().order_by('data')
      lista_consultas_ordenada = []
      consultas_comuns = []
      consultas_preferenciais = []
      for consulta in consultas:
          if consulta.paciente.descricao == 'preferencial':
              consultas_preferenciais.append(consulta)
          else:
              consultas_comuns.append(consulta)
      lista_consultas_ordenada.extend(consultas_preferenciais)
      for i, consulta_preferencial in enumerate(consultas_comuns):
          index = (i + 1) * 1 + i 
          lista_consultas_ordenada.insert(index, consulta_preferencial)
      return lista_consultas_ordenada
      nome = self.request.GET.get('nome')
      if nome:
            consultas_filtradas = Consulta.objects.filter(nome__icontains=nome)
      else:
            consultas_filtradas = Consulta.objects.all()
        
      return consultas_filtradas



class ComentarioCreate(CreateView):
    login_url = reverse_lazy('login')
    model = Comentario
    fields = ['sugestoes','nota']
    template_name = 'form.html'
    success_url = reverse_lazy('Listar-comentario')
    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['Titulo'] = ' deixe sua sugestão '
      context['conteudo'] = 'de uma nota de 0 a 100'
      return context
class ComentarioList(ListView):
    model = Comentario
    template_name = 'listas/comentario.html'
    paginate_by = 5

    