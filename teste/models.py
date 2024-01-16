from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=14, null=False)
    email = models.EmailField()

    def __str__(self):
        return self.nome + '-' + self.email
    
class Curso(models.Model):
    nome_curso = models.CharField(max_length=200, null=False)
    carga_horaria = models.CharField(max_length=8, null=False)
    investimento = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nome_curso + '-' + self.carga_horaria + '-' + self. investimento
    
