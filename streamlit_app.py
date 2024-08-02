import streamlit as st
from main import ResearchCrew  # Importar a classe ResearchCrew de main.py
import os

st.title('Configuração da Equipe de Pesquisa')
os.environ["OPENAI_API_KEY"] = "SUA CHAVE DE API AQUI"
os.environ["SERPER_API_KEY"] = "SUA CHAVE DE API AQUI"

with st.sidebar:
    st.header('Insira os Detalhes da Pesquisa')
    topic = st.text_input("Tópico principal da sua pesquisa:")
    detailed_questions = st.text_area("Perguntas específicas ou subtópicos que você está interessado em explorar:")
    key_points = st.text_area("Pontos chave ou informações específicas necessárias:")

if st.button('Executar Pesquisa'):
    if not topic or not detailed_questions or not key_points:
        st.error("Por favor, preencha todos os campos.")
    else:
        inputs = f"Tópico da Pesquisa: {topic}\nPerguntas Detalhadas: {detailed_questions}\nPontos Chave: {key_points}"
        research_crew = ResearchCrew(inputs)
        result = research_crew.run()
        st.subheader("Resultados do seu projeto de pesquisa:")
        st.write(result)
