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
    telefone = models.IntegerField (verbose_name='telefone')
    numero_sus = models.IntegerField (verbose_name='numero_sus')
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=150, verbose_name="descricao")
    sintomas = models.CharField(max_length=150, verbose_name="simtomas")
    doença_cronica = models.CharField(max_length=150, verbose_name="doença_cronica", null =True ,blank = True)
    idade = models.IntegerField (verbose_name='idade')
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.hospital)


class Cronograma(models.Model):
    usuario  = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50 , verbose_name = 'nome')
    data= models.CharField (verbose_name='data', max_length = 10)
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
    horario= models.CharField( verbose_name="horario" , max_length=15 )
    status = models.CharField( verbose_name ='status' ,max_length=20,  null =True ,blank = True )
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.data)
class Comentario(models.Model):
       nota = models.IntegerField (verbose_name='nota')
       sugestoes = models.TextField( verbose_name ='sugestoes', max_length=255 )
       def __str__(self):
           return "{} ({})".format(self.nota, self.sugestão)
class Triagem(models.Model):
    usuario  = models.ForeignKey(User, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente,on_delete = models.PROTECT)
    data = models.CharField (verbose_name='data', max_length = 10)
    medico = models.ForeignKey (Medico, on_delete=models.PROTECT)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)
    horario= models.CharField( verbose_name="horario" , max_length=15 )
    pressao = models.CharField( verbose_name ='pressao' ,max_length=20, )
    def __str__(self):
       return "{}".format(self.paciente.nome)

    
     