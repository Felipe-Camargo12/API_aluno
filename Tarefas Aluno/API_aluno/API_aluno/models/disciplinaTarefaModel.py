from django.db import models
from API_aluno.models.disciplinaModel import DisciplinaModel
from API_aluno.models.tarefaModel import TarefaModel

# Definição de um modelo chamado DisciplinaTarefaModel
class DisciplinaTarefaModel(models.Model):
    # Campo de chave estrangeira referenciando o modelo TarefaModel
    tarefa = models.ForeignKey(TarefaModel, on_delete=models.CASCADE)
    
    # Campo de chave estrangeira referenciando o modelo DisciplinaModel
    disciplina = models.ForeignKey(DisciplinaModel, on_delete=models.CASCADE)
