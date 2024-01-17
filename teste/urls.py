from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #Alunos
    path('listar_alunos', views.listarAluno, name='listar_alunos'),

    #Curso
    path('listar_cursos', views.listarCurso, name='listar_cursos')
]