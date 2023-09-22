"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from API_aluno.view.alunoView import AlunoView
from API_aluno.view.detalheAlunoView import DetalheAlunoView
from API_aluno.view.detalheTarefaView import DetalheTarefaView
from API_aluno.view.detalheDisciplinaView import DetalheDisciplinaView
from API_aluno.view.tarefaView import TarefaView
from API_aluno.view.disciplinaView import DisciplinaView
from API_aluno.view.alunoTarefa import ListaTarefasAluno


urlpatterns = [
    path('api/alunos/', AlunoView.as_view()),
    path('api/alunos/<int:pk>/', DetalheAlunoView.as_view()),
    path('api/disciplinas/', DisciplinaView.as_view()),
    path('api/disciplinas/<int:pk>/', DetalheDisciplinaView.as_view()),
    path('api/tarefas/', TarefaView.as_view()),
    path('api/tarefas/<int:pk>/', DetalheTarefaView.as_view()),
    path('api/alunos/<int:pk>/tarefas/', ListaTarefasAluno.as_view()),
]
