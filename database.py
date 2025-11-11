from models import Competencia, Carreira

C_PYTHON = Competencia(nome="Python", tipo="tecnica")
C_IA = Competencia(nome="Inteligência Artificial", tipo="tecnica")
C_DADOS = Competencia(nome="Análise de Dados", tipo="tecnica")
C_AUTOMACAO = Competencia(nome="Automação de Processos", tipo="tecnica")
C_DESIGN_UX = Competencia(nome="Design de UX/UI", tipo="tecnica")

C_LOGICA = Competencia(nome="Lógica", tipo="comportamental")
C_CRIATIVIDADE = Competencia(nome="Criatividade", tipo="comportamental")
C_COLABORACAO = Competencia(nome="Colaboração", tipo="comportamental")
C_ADAPTABILIDADE = Competencia(nome="Adaptabilidade", tipo="comportamental")
C_COMUNICACAO = Competencia(nome="Comunicação", tipo="comportamental")

TODAS_AS_COMPETENCIAS = [
    C_PYTHON, C_IA, C_DADOS, C_AUTOMACAO, C_DESIGN_UX,
    C_LOGICA, C_CRIATIVIDADE, C_COLABORACAO, C_ADAPTABILIDADE, C_COMUNICACAO
]

LISTA_DE_CARREIRAS = [
    Carreira(
        nome="Engenheiro de Prompt (IA)",
        descricao="Especialista em criar e otimizar inputs para IAs generativas.",
        competencias_necessarias={C_IA, C_CRIATIVIDADE, C_LOGICA, C_COMUNICACAO}
    ),
    Carreira(
        nome="Analista de Dados Quânticos",
        descricao="Profissional que usa computação quântica para analisar grandes volumes de dados.",
        competencias_necessarias={C_DADOS, C_IA, C_LOGICA, C_ADAPTABILIDADE}
    ),
    Carreira(
        nome="Especialista em Automação e RPA",
        descricao="Desenvolve robôs (bots) para automatizar tarefas de negócios repetitivas.",
        competencias_necessarias={C_AUTOMACAO, C_PYTHON, C_LOGICA, C_COLABORACAO}
    ),
    Carreira(
        nome="Designer de Experiência de Realidade Mista",
        descricao="Projeta interfaces e experiências para óculos de AR e VR.",
        competencias_necessarias={C_DESIGN_UX, C_CRIATIVIDADE, C_ADAPTABILIDADE, C_COLABORACAO}
    )
]