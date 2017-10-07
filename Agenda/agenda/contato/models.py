from django.db import models

class Contato(models.Model):

    SEXO_CHOICES = (
        (u'masculino', u'Masculino'),
        (u'feminino', u'Feminino'),
    )

    ESTADO_CIVIL_CHOICES = (
        (u'solteiro', u'Solteiro'),
        (u'casado', u'Casado'),
        (u'divorciado', u'Divorciado'),
        (u'viuvo', u'Viuvo'),
    )
    
    contato_id = models.AutoField(primary_key=True)
    contato_nome = models.CharField(max_length=45)
    contato_nascimento = models.DateField()
    contato_sexo  = models.CharField(max_length=50, choices=SEXO_CHOICES)
    contato_estado_civil = models.CharField(max_length=50, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado Civil')
    contato_email = models.CharField(max_length=50)
    contato_favorito = models.BooleanField(verbose_name='Favorito')

class Tarefas(models.Model):

    tarefa_id = models.AutoField(primary_key=True)
    tarefa_nome = models.CharField(max_length=120)
    tarefa_data_inicio = models.DateField()
    conclusao = models.BooleanField(verbose_name='Concluido')

