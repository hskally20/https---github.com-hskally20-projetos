from django.urls import path
from .views import HospitalCreate, MedicoCreate , PacienteCreate , CronogramaCreate , ConsultaCreate, ComentarioCreate , TriagemCreate , ProntuarioCreate
from .views import  HospitalUpdate, MedicoUpdate , PacienteUpdate,CronogramaUpdate , ConsultaUpdate ,Consulta2Update, TriagemUpdate , ProntuarioUpdate
from .views import  HospitalDelete,MedicoDelete , PacienteDelete , CronogramaDelete, ConsultaDelete, TriagemDelete , ProntuarioDelete
from .views import  HospitalList,MedicoList ,PacienteList ,CronogramaList ,ConsultaList,ComentarioList,TriagemList, NotificacaoList ,ProntuarioList
from .views import ChamarPacienteView




urlpatterns = [
    path('cadastrar/hospital/', HospitalCreate.as_view(),
        name='cadastrar-hospital'),
    path('cadastrar/medico/', MedicoCreate.as_view(),
        name='cadastrar-medico'),
    path('cadastrar/paciente/', PacienteCreate.as_view(),
        name='cadastrar-paciente'),
    path('cadastrar/cronograma/', CronogramaCreate.as_view(),
        name='cadastrar-cronograma'),
    path('cadastrar/consulta/', ConsultaCreate.as_view(),
        name='cadastrar-consulta'),
   
    path('cadastrar/comentario/', ComentarioCreate.as_view(),
        name='cadastra-comentario'),
     path('cadastrar/triagem/', TriagemCreate.as_view(),
        name='cadastrar-triagem'),
    path('cadastrar/prontuario/', ProntuarioCreate.as_view(),
        name='cadastrar-prontuario'),

    path('editar/hospital/<int:pk>', HospitalUpdate.as_view(),
        name='editar-hospital'),
    path('editar/medico/<int:pk>',MedicoUpdate.as_view(),
        name='editar-medico'),
    path('editar/paciente/<int:pk>', PacienteUpdate.as_view(),
        name='editar-paciente'),
    path('editar/cronograma/<int:pk>', CronogramaUpdate.as_view(),
        name='editar-cronograma'),

    path('editar/consulta/<int:pk>', ConsultaUpdate.as_view(),
        name='editar-consulta'),

    path('editar/consulta2/<int:pk>', Consulta2Update.as_view(),
        name='editar-consulta2'),

    path('editar/triagem/<int:pk>', TriagemUpdate.as_view(),
            name='editar-triagem'),

    path('editar/Prontuario/<int:pk>', ProntuarioUpdate.as_view(),
            name='editar-triagem'),
    

    
    path('excluir/hospital/<int:pk>', HospitalDelete.as_view(),
        name='excluir-hospital'),
    path('excluir/medico/<int:pk>',MedicoDelete.as_view(),
        name='excluir-medico'),
    path('excluir/paciente/<int:pk>', PacienteDelete.as_view(),
        name='excluir-paciente'),
    path('excluir/cronograma/<int:pk>', CronogramaDelete.as_view(),
        name='excluir-cronograma'),
    path('excluir/consulta/<int:pk>',ConsultaDelete.as_view(),
        name='excluir-consulta'),
    path('excluir/triagem/<int:pk>',TriagemDelete.as_view(),
        name='excluir-triagem'),
    path('excluir/Prontuario/<int:pk>',ProntuarioDelete.as_view(),
        name='excluir-triagem'),
    
    path('listar/hospital/', HospitalList.as_view(),
        name='listar-hospital'),
    path('listar/Medico/', MedicoList.as_view(),
        name='listar-medico'),
    path('listar/paciente/', PacienteList.as_view(),
        name='Listar-paciente'),
    path('listar/cronograma/',CronogramaList.as_view(),
        name='Listar-cronograma'),
    path('listar/consulta/',ConsultaList.as_view(),
    name='Listar-consulta'),
    path('listar/comentario/',ComentarioList.as_view(),
    name='Listar-comentario'),
    path('listar/triagem/',TriagemList.as_view(),
    name='Listar-triagem'),
   
    path('listar/notificacao/',NotificacaoList.as_view(),
    name='Listar-notificacao'),
    path('listar/Prontuario/', ProntuarioList.as_view(),
    name='Listar-Prontuario'),
    
    path('chamar-paciente/', ChamarPacienteView.as_view(), name='chamar-paciente'),


]