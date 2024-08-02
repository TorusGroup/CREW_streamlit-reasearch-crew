from crewai import Task

class ResearchCrewTasks:

    def tarefa_de_pesquisa(self, agente, inputs):
        return Task(
            agent=agente,
            description=f"Reunir e documentar sistematicamente notícias e artigos atuais e relevantes de diversas fontes sobre {inputs}. Use todas as ferramentas digitais disponíveis para garantir uma cobertura abrangente.",
            expected_output=f"""
  Relatório Detalhado de Pesquisa sobre {inputs}
  1. **Resumo Executivo**: Uma visão geral concisa das descobertas da pesquisa, destacando os insights e conclusões mais críticos derivados dos dados coletados.
  2. **Introdução**: Informações de fundo sobre por que a pesquisa sobre {inputs} é crucial neste momento. Incluir o escopo da pesquisa e os principais objetivos.
  3. **Metodologia**:
    - **Fontes Utilizadas**: Listar todas as fontes utilizadas, incluindo bancos de dados digitais, sites de notícias e quaisquer assinaturas ou ferramentas especializadas.
    - **Critérios de Pesquisa**: Descrever os critérios de pesquisa e palavras-chave usadas para coletar as informações relevantes.
    - **Processo de Coleta de Dados**: Descrever os passos tomados no processo de coleta de dados, incluindo quaisquer ferramentas ou softwares de automação utilizados.
  4. **Descobertas**:
    - **Informações Chave Reunidas**: Resumir as principais informações coletadas de cada fonte, categorizadas por relevância e impacto no tópico.
    - **Temas Identificados**: Discutir quaisquer temas recorrentes ou similaridades encontradas em diferentes fontes.
  5. **Análise**:
    - **Relevância para Tendências Atuais**: Analisar como as descobertas se relacionam com tendências ou desenvolvimentos atuais no campo.
    - **Lacunas de Informação**: Destacar quaisquer lacunas notáveis nas informações que possam exigir mais pesquisa.
  6. **Conclusão**:
    - **Resumo das Descobertas**: Reiterar brevemente as descobertas mais críticas e suas implicações.
    - **Recomendações para Pesquisas Futuras**: Sugerir áreas onde investigação adicional poderia ser benéfica com base nas lacunas ou tendências emergentes observadas durante a pesquisa.
  7. **Referências**:
    - **Citações Completas**: Fornecer citações completas para todas as fontes usadas, formatadas de acordo com um padrão acadêmico reconhecido.
            """
        )

    def tarefa_de_analise(self, agente, contexto):
        return Task(
            agent=agente,
            context=contexto,
            description="Avaliar criticamente a precisão, relevância e profundidade das informações coletadas. Empregar metodologias avançadas de análise de dados para melhorar o valor das informações, garantindo que atendam aos altos padrões exigidos para avaliação especializada.",
            expected_output=f"""
  Relatório de Análise Compreensiva:
  1. **Resumo Executivo**: Uma visão geral que resume as principais descobertas, incluindo a precisão, relevância e profundidade das informações analisadas.
  2. **Avaliação da Precisão**:
    - **Verificação de Dados**: Avaliar a veracidade e correção dos dados coletados, identificando quaisquer discrepâncias ou inconsistências.
    - **Confiabilidade das Fontes**: Avaliar a confiabilidade das fontes utilizadas, fornecendo uma pontuação de credibilidade para cada uma.
  3. **Análise de Relevância**:
    - **Alinhamento Contextual**: Analisar como as informações se alinham com as perguntas e objetivos atuais da pesquisa.
    - **Atualidade**: Verificar se as informações estão atualizadas e discutir sua significância no contexto atual.
  4. **Avaliação de Profundidade**:
    - **Abrangência**: Avaliar o escopo das informações e se elas cobrem todos os aspectos necessários do tópico.
    - **Perspicácia**: Avaliar a profundidade dos insights fornecidos pelas informações, incluindo quaisquer implicações subjacentes ou padrões ocultos.
  5. **Revisão Metodológica**:
    - **Técnicas Utilizadas**: Descrever e criticar as metodologias de análise de dados empregadas, sugerindo melhorias ou alternativas, se necessário.
    - **Manipulação de Dados**: Discutir como os dados foram processados e analisados, incluindo quaisquer ferramentas ou softwares utilizados.
  6. **Recomendações**:
    - **Pesquisas Futuras**: Sugerir áreas onde informações adicionais são necessárias e propor métodos para coletar esses dados.
    - **Aplicações Práticas**: Fornecer recomendações sobre como as descobertas podem ser utilizadas de forma prática por partes interessadas ou em pesquisas futuras.
  7. **Conclusão**:
    - **Resumo dos Pontos Chave**: Reiterar de forma concisa as descobertas mais importantes e suas implicações para o projeto de pesquisa.
    - **Direções Futuras**: Sugerir como as descobertas podem informar pesquisas futuras e processos de tomada de decisão no campo relevante.
  8. **Apêndices**:
    - **Tabelas e Figuras de Dados**: Incluir tabelas, gráficos e diagramas abrangentes que foram usados na análise.
    - **Documentação das Fontes**: Fornecer citações detalhadas e referências para todas as fontes e dados usados no relatório.
            """
        )

    def tarefa_de_escrita(self, agente, contexto):
        return Task(
            agent=agente,
            context=contexto,
            description="Sintetizar as informações fornecidas pelo Pesquisador e aprimoradas pelo Analista em um resumo claro, convincente e bem estruturado. Incluir as principais descobertas e citar todas as fontes apropriadamente para garantir credibilidade e rastreabilidade.",
            expected_output=f"""
    Relatório de Resumo Compreensivo:
    1. **Introdução**:
      - **Contexto**: Fornecer uma breve introdução ao tópico, delineando o escopo e o propósito da pesquisa inicial.
      - **Objetivos**: Recapitular os principais objetivos da pesquisa para definir o contexto das descobertas.

    2. **Síntese da Pesquisa e Análise**:
      - **Principais Descobertas**: Apresentar as principais descobertas da fase de pesquisa, enfatizando pontos de dados significativos, tendências e insights.
      - **Aprimoramentos Analíticos**: Discutir como a fase de análise agregou valor às descobertas iniciais, incluindo quaisquer novos insights ou entendimentos derivados de um exame mais profundo.

    3. **Discussão**:
      - **Implicações**: Explorar as implicações das descobertas em um contexto mais amplo, discutindo potenciais impactos no campo, indústria ou sociedade.
      - **Avaliação Crítica**: Avaliar criticamente as descobertas, observando pontos fortes, fraquezas e quaisquer pontos controversos que surgiram durante as fases de pesquisa e análise.

    4. **Recomendações**:
      - **Passos Práticos**: Fornecer recomendações práticas e acionáveis baseadas nas descobertas e discussões. Estas devem ser práticas e adaptadas a partes interessadas específicas ou implicações políticas.
      - **Pesquisas Futuras**: Sugerir áreas para futuras pesquisas que possam construir sobre as descobertas atuais, abordando quaisquer lacunas ou questões não resolvidas.

    5. **Conclusão**:
      - **Resumo das Descobertas**: Resumir os principais pontos do relatório, reforçando a significância e confiabilidade da pesquisa realizada.
      - **Considerações Finais**: Oferecer considerações finais que enfatizem a importância das descobertas e o potencial para trabalhos futuros nesta área.

    6. **Referências**:
      - **Citações**: Incluir uma lista detalhada de todas as fontes citadas no documento, formatadas de acordo com um padrão acadêmico ou profissional reconhecido.
      - **Anotações das Fontes**: Opcionalmente, fornecer anotações para fontes chave, explicando sua relevância e confiabilidade.

    7. **Apêndices** (se aplicável):
      - **Documentos de Suporte**: Anexar quaisquer documentos de suporte, tabelas de dados ou material suplementar referenciado no relatório.
      - **Glossário de Termos**: Incluir um glossário de termos chave e definições usados ao longo do relatório para maior clareza.
            """
        )
