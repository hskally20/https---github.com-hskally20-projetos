from django.urls import path
from .views import IndexView ,SugestoesView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # login 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view (),  name='logout'),

    #cadastros 
    path('', IndexView.as_view(), name='inicio'),
    path('cadastrar-paciente', IndexView.as_view(), name='cadastrar-paciente'),
    path('cadastrar-hospital', IndexView.as_view(), name='cadastrar-hospital'),
    path('cadastrar-medico', IndexView.as_view(), name='cadastrar-medico'),
    path('cadastrar-cronograma', IndexView.as_view(), name='cadastrar-cronograma'),
    path('cadastrar-consulta', IndexView.as_view(), name='cadastrar-consulta'),
    path('cadastrar-comentario', IndexView.as_view(), name='cadastrar-comentario'),

    #listas
    path('listar-hospital', IndexView.as_view(), name='listar-hospital'),
    path('listar-Medico', IndexView.as_view(), name='listar-Medico'),
    
    path('Listar-cronograma', IndexView.as_view(), name='Listar-cronograma'),
    path('Listar-consulta', IndexView.as_view(), name='Listar-consulta'),
     path('Listar-comentario', IndexView.as_view(), name='Listar-comentario'),
    # deletes
    path('excluir-hospital', IndexView.as_view(), name='excluir-hospital'),
    path('excluir-medico', IndexView.as_view(), name='excluir-medico'),
    path('excluir-paciente', IndexView.as_view(), name='excluir-paciente'),
    path('excluir-cronograma', IndexView.as_view(), name='excluir-cronograma'),
    path('excluir-consulta', IndexView.as_view(), name='excluir-consulta'),
    # editar
    path('editar-hospital', IndexView.as_view(), name='editar-hospital'),
    path('editar-medico', IndexView.as_view(), name='editar-medico'),
    path('editar-paciente', IndexView.as_view(), name='editar-paciente'),
    path('editar-cronograma', IndexView.as_view(), name='editar-cronograma'),
    path('editar-consulta', IndexView.as_view(), name='editar-consulta'),

    #sugestoes

     path('sugestoes/',SugestoesView.as_view(), name='sugestoes'),
]