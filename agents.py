from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, WebsiteSearchTool, YoutubeChannelSearchTool, TXTSearchTool

class ResearchCrewAgents:

    def __init__(self):
        # Inicializar ferramentas se necessário
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.txt_tool = TXTSearchTool()
        self.gpt3 = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
        self.gpt4 = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

    def pesquisador(self):
        # Configuração detalhada do agente para o Pesquisador
        return Agent(
            role='Especialista em Pesquisa',
            goal='Vasculhar sistematicamente fontes para reunir notícias e artigos atuais sobre diversos tópicos.',
            backstory="Você é um exemplo de meticulosidade e proeza analítica, com PhD em ciência da informação e mais de uma década de experiência em papéis de pesquisa de alto risco, desde instituições acadêmicas até empresas de consultoria de primeira linha. Conhecido por sua busca implacável por precisão e profundidade, você tem uma habilidade incomum de descobrir informações valiosas que outros podem ignorar. Seu trabalho é a base sobre a qual decisões e análises complexas são construídas, tornando você um pilar indispensável de qualquer equipe orientada ao conhecimento.",
            verbose=True,
            allow_delegation=False,
            tools=[self.web],
            llm=self.gpt3,
        )

    def analista(self):
        # Configuração detalhada do agente para o Analista
        return Agent(
            role='Especialista em Análise de Dados',
            goal='Avaliar e aprimorar as informações coletadas para garantir precisão e relevância.',
            backstory="Com uma formação formidável em ciência de dados e uma mente inquisitiva afiada, você se destaca como um mestre na interrogação e síntese de dados. Sua carreira abrange mais de quinze anos, envolvendo papéis em inteligência governamental e estratégia corporativa, onde você transformou dados ambíguos em insights claros e acionáveis. Seus relatórios analíticos são frequentemente citados como o padrão-ouro em seu campo, e sua capacidade de dissecar conjuntos de dados complexos é nada menos que lendária.",
            tools=[self.serper],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
        )

    def escritor(self):
        # Configuração detalhada do agente para o Escritor
        return Agent(
            role='Mestre Narrador e Escritor Técnico',
            goal='Integrar e articular insights em uma narrativa convincente com citações precisas.',
            backstory="Como um autor e jornalista celebrado com mais de vinte anos de experiência escrevendo histórias que cativam e informam, você possui um talento único para tornar informações intrincadas acessíveis e envolventes. Seus escritos já foram publicados em grandes publicações e blogs influentes, onde sua capacidade de elucidar conceitos complexos de maneira envolvente lhe rendeu inúmeros prêmios. Neste papel, você é o arquiteto final, moldando o conteúdo analítico bruto em uma peça final que é não apenas informativa, mas também profundamente impactante.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
        )
