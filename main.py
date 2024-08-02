import os
from decouple import config
from crewai import Crew, Process
from textwrap import dedent
from agents import ResearchCrewAgents
from tasks import ResearchCrewTasks

# Configurar variáveis de ambiente
os.environ["OPENAI_API_KEY"] = "SUA CHAVE DE API AQUI"
os.environ["SERPER_API_KEY"] = "SUA CHAVE DE API AQUI"

class ResearchCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = ResearchCrewAgents()
        self.tasks = ResearchCrewTasks()

    def run(self):
        # Inicializar agentes
        researcher = self.agents.researcher()
        analyst = self.agents.analyst()
        writer = self.agents.writer()

        # Inicializar tarefas com respectivos agentes
        research_task = self.tasks.research_task(researcher, self.inputs)
        analysis_task = self.tasks.analysis_task(analyst, [research_task])
        writing_task = self.tasks.writing_task(writer, [analysis_task])

        # Formar a equipe com os agentes e tarefas definidos
        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential
        )

        # Executar a equipe para realizar o projeto de pesquisa
        return crew.kickoff()

if __name__ == "__main__":
    print("Bem-vindo à Configuração da Equipe de Pesquisa")
    print("---------------------------------------")
    topic = input("Por favor, insira o tópico principal da sua pesquisa: ")
    detailed_questions = input("Quais perguntas específicas ou subtópicos você está interessado em explorar? ")
    key_points = input("Há algum ponto chave ou informação específica que você precisa incluir na pesquisa? ")

    inputs = f"Tópico da Pesquisa: {topic}\nPerguntas Detalhadas: {detailed_questions}\nPontos Chave: {key_points}"
    research_crew = ResearchCrew(inputs)
    result = research_crew.run()

    print("\n\n##############################")
    print("## Aqui estão os resultados do seu projeto de pesquisa:")
    print("##############################\n")
    print(result)
