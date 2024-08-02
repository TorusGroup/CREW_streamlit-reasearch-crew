import os
from decouple import config
from crewai import Crew, Process
from textwrap import dedent
from agents import ResearchCrewAgents
from tasks import ResearchCrewTasks

# Configurar variáveis de ambiente
os.environ["OPENAI_API_KEY"] = "SUA CHAVE DE API AQUI"
os.environ["SERPER_API_KEY"] = "SUA CHAVE DE API AQUI"

class EquipeDePesquisa:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = ResearchCrewAgents()
        self.tasks = ResearchCrewTasks()

    def run(self):
        # Inicializar agentes
        pesquisador = self.agents.researcher()
        analista = self.agents.analyst()
        escritor = self.agents.writer()

        # Inicializar tarefas com respectivos agentes
        tarefa_de_pesquisa = self.tasks.research_task(pesquisador, self.inputs)
        tarefa_de_analise = self.tasks.analysis_task(analista, [tarefa_de_pesquisa])
        tarefa_de_escrita = self.tasks.writing_task(escritor, [tarefa_de_analise])

        # Formar a equipe com os agentes e tarefas definidos
        equipe = Crew(
            agents=[pesquisador, analista, escritor],
            tasks=[tarefa_de_pesquisa, tarefa_de_analise, tarefa_de_escrita],
            process=Process.sequential
        )

        # Executar a equipe para realizar o projeto de pesquisa
        return equipe.kickoff()

if __name__ == "__main__":
    print("Bem-vindo à Configuração da Equipe de Pesquisa")
    print("---------------------------------------")
    topico = input("Por favor, insira o tópico principal da sua pesquisa: ")
    perguntas_detalhadas = input("Quais perguntas específicas ou subtópicos você está interessado em explorar? ")
    pontos_chave = input("Há algum ponto chave ou informação específica que você precisa incluir na pesquisa? ")

    inputs = f"Tópico da Pesquisa: {topico}\nPerguntas Detalhadas: {perguntas_detalhadas}\nPontos Chave: {pontos_chave}"
    equipe_de_pesquisa = EquipeDePesquisa(inputs)
    resultado = equipe_de_pesquisa.run()

    print("\n\n##############################")
    print("## Aqui estão os resultados do seu projeto de pesquisa:")
    print("##############################\n")
    print(resultado)
