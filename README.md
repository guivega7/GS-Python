# 🚀 Future at Work - Global Solution 2025.2

[cite_start]Projeto de "Pensamento Computacional e Automação com Python" [cite: 5] [cite_start]para a Global Solution da FIAP, com o tema "Future at Work"[cite: 2].

---

## 🎯 Descrição do Projeto

[cite_start]O **Future at Work** é um sistema de linha de comando (CLI) em Python que simula uma ferramenta inteligente de orientação de carreiras[cite: 7]. [cite_start]O objetivo é conectar as competências (técnicas e comportamentais) de um usuário com carreiras do futuro[cite: 8].

[cite_start]Com base no perfil cadastrado, o sistema gera recomendações personalizadas [cite: 9][cite_start], indicando o percentual de compatibilidade e quais competências faltam para o usuário se aprimorar (trilha de aprendizado)[cite: 9].

### Funcionalidades Principais
* **Cadastro de Perfil:** O usuário pode inserir seu nome e selecionar suas competências atuais de uma lista.
* **Ver Recomendações:** O sistema analisa o perfil e o compara com uma base de dados de carreiras.
* [cite_start]**Gerar Trilha de Aprendizado:** Ao listar uma carreira, o sistema mostra as competências que o usuário já possui e as que faltam para atingir 100% de compatibilidade[cite: 9].

## 🛠️ Instruções de Execução

**Pré-requisitos:**
* Ter o Python 3.x instalado.

**Como rodar:**
1.  Clone este repositório para sua máquina local.
2.  Abra um terminal na pasta raiz do projeto.
3.  Execute o arquivo principal:
    ```bash
    python main.py
    ```
4.  Siga as instruções do menu que aparecerá no terminal.

## 📂 Estrutura de Arquivos e Classes

[cite_start]O projeto é organizado em módulos, seguindo os princípios de Orientação a Objetos e separação de responsabilidades[cite: 13, 15]:

* **`main.py`**
    * É o ponto de entrada da aplicação.
    * [cite_start]Contém a interface de linha de comando (CLI) [cite: 17] e o menu principal.
    * Gerencia o fluxo de `cadastrar_perfil()` e `mostrar_recomendacoes()`.

* **`models.py`**
    * [cite_start]Define as classes e estruturas de dados do sistema[cite: 15], usando `dataclasses` para clareza.
    * **`Competencia`**: Armazena o nome e o tipo (técnica/comportamental) de uma competência.
    * **`Carreira`**: Armazena o nome, descrição e o conjunto (`Set`) de competências necessárias.
    * **`Perfil`**: Armazena o nome do usuário e o conjunto (`Set`) de suas competências.

* **`logic.py`**
    * [cite_start]Contém a lógica principal do sistema[cite: 16].
    * **`gerar_recomendacoes()`**: Função que recebe o perfil e a lista de carreiras. Ela calcula o percentual de *match* (usando interseção de conjuntos) e identifica as competências faltantes (usando diferença de conjuntos).

* **`database.py`**
    * Atua como um banco de dados simulado (em memória).
    * `TODAS_AS_COMPETENCIAS`: Lista de objetos `Competencia` disponíveis para o usuário escolher.
    * `LISTA_DE_CARREIRAS`: Lista de objetos `Carreira` que o sistema usa para comparar com o perfil.

## 👤 Autor

* **Guilherme Vega** - RM: **562655**
* **Gabriel Pereira** - RM: **563795**
* **Luiz Henrique** - RM: **563571**