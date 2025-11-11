# 🚀 Future at Work — Global Solution 2025.2
Projeto do curso "Pensamento Computacional e Automação com Python" (Global Solution — FIAP) com o tema "Future at Work".

---
## 🎯 Descrição
`Future at Work` é uma aplicação de linha de comando (CLI) em Python que ajuda a conectar competências (técnicas e comportamentais) de um usuário com potenciais carreiras do futuro. A partir do perfil cadastrado, o sistema gera recomendações mostrando o percentual de compatibilidade e as competências que faltam para alcançar 100% de aderência a cada carreira.

### Funcionalidades principais
- Cadastro de perfil (nome + competências selecionadas)
- Recomendações de carreiras com percentual de compatibilidade
- Geração de trilha de aprendizado (competências faltantes)
## 🛠️ Requisitos
- Python 3.8+ (ou Python 3.x)
## ▶ Como executar
1. Clone o repositório:
```powershell
git clone https://github.com/guivega7/GS-Python.git
cd "GS-Python"
```

2. Execute o programa:

```powershell
python main.py
```

3. Siga as instruções exibidas no menu do terminal.

> Dica: recomenda-se criar um ambiente virtual (venv) para isolar dependências, caso venha a adicionar pacotes externos.
## 📁 Estrutura do projeto

- `main.py` — ponto de entrada e interface CLI
- `database.py` — banco de dados em memória (lista de carreiras e competências)
- `models.py` — classes de dados (Competência, Carreira, Perfil)
- `logic.py` — funções principais para gerar recomendações e calcular compatibilidade
- `.gitignore` — arquivos ignorados pelo Git
## 👥 Autores

- Guilherme Vega — RM 562655
- Gabriel Pereira — RM 563795
- Luiz Henrique — RM 563571

