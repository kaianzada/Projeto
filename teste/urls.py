from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #Alunos
    path('listar_alunos', views.listarAluno, name='listar_alunos'),
    path('incluir_aluno', views.incluirAluno, name='incluir_aluno'),
    path('editar_aluno/<int:id>', views.editarAluno, name='editar_aluno'),
    #Curso
    path('listar_cursos', views.listarCurso, name='listar_cursos'),
    path('incluir_curso', views.incluirCurso, name='incluir_curso'),
    path('editar_curso/<int:id>', views.editarCurso, name='editar_curso')
]