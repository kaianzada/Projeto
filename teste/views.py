from django.shortcuts import render
from django.http import HttpResponse

from teste.models import Aluno, Curso

# Create your views here.
def index(request):
    return HttpResponse("Olá Mundo! Agora é na web")

def listarAluno(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_aluno.html', {'alunos': alunos})

def listarCurso(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_curso.html', {'cursos': cursos})
    