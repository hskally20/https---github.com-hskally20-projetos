from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hospital(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150,
        verbose_name="descricao")
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class Medico(models.Model):
    usuario  = models.ForeignKey(User, on_delete=models.PROTECT)
    numero = models.IntegerField(verbose_name="Número de telefone")
    nome = models.CharField(max_length=50, verbose_name=" nome")
    cpf = models.CharField(max_length = 11 ,verbose_name=" cpf ")
    especificacao = models.CharField(max_length=150)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self. especificacao, self.hospital.nome)

class Paciente(models.Model):
    usuario  = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    telefone = models.CharField (verbose_name='telefone', max_length=11)
    numero_sus = models.CharField (verbose_name='numero_sus', max_length=15)
    cpf = models.CharField(verbose_name='cpf', max_length=11, null=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=150, verbose_name="descricao")
    sintomas = models.CharField(max_length=150, verbose_name="sintomas")
    doença_cronica = models.CharField(max_length=150, verbose_name="doença_cronica", null =True ,blank = True)
    idade = models.IntegerField (verbose_name='idade')
    usuario = models.ForeignKey(User, related_name='pacientes', on_delete=models.CASCADE)
    
    # Define o campo 'usuario_cadastrador' que refere-se ao usuário que cadastrou o paciente.
    usuario_cadastrador = models.ForeignKey(User, related_name='pacientes_cadastrados', on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.hospital)


class Cronograma(models.Model):
    usuario  = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50 , verbose_name = 'nome')
    data= models.DateField(verbose_name='data', max_length = 10)
    medico = models.ForeignKey (Medico, on_delete=models.PROTECT)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)
    horario= models.CharField( verbose_name="orario" , max_length=15 )
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.orario)

    
class Consulta(models.Model):
    usuario  = models.ForeignKey(User, on_delete=models.PROTECT)
    nome ="consulta"
    paciente = models.ForeignKey(Paciente,on_delete = models.PROTECT)
    data = models.CharField (verbose_name='data', max_length = 10)
    medico = models.ForeignKey (Medico, on_delete=models.PROTECT)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)
    status = models.CharField( verbose_name ='status' ,max_length=20,  null =True ,blank = True )
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.data)
class Comentario(models.Model):
       nota = models.IntegerField (verbose_name='nota')
       sugestoes = models.TextField( verbose_name ='sugestoes', max_length=255 )
       def __str__(self):
           return "{} ({})".format(self.nota, self.sugestão)

class Triagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    data = models.DateTimeField(verbose_name='data')  # Change to DateTimeField for datetime input
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)
    horario = models.TimeField(verbose_name="horario", default='09:00:00')  # Set default time
    pressao = models.CharField(verbose_name='pressao', max_length=20)
    temperatura = models.FloatField(verbose_name='temperatura')
    peso = models.FloatField(verbose_name='peso_corporal')
    glicose = models.CharField(verbose_name='glicose', max_length=6, null=True, blank=True)
    
    def __str__(self):
        return "{}".format(self.paciente.nome)
 
class Notificacao(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return self.mensagem
class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)  
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    remedio = models.CharField(verbose_name ='remedio' ,max_length=255)
    diagnostico = models.TextField(verbose_name='diagnostico' , max_length=255)
    recomendacoes = models.TextField(verbose_name = 'recomendacoes', max_length=255 ,null=True, blank=True)
    def __str__(self):
      return print('prontuario')
