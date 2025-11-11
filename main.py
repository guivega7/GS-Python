import time
from models import Perfil
from database import TODAS_AS_COMPETENCIAS, LISTA_DE_CARREIRAS
from logic import gerar_recomendacoes

def exibir_menu_competencias():
    """Mostra todas as competências disponíveis para seleção."""
    print("\n--- Lista de Competências Disponíveis ---")
    print("Digite os números das competências que você possui, separados por vírgula.")
    
    # Usamos enumerate para gerar os índices (começando do 1)
    for i, competencia in enumerate(TODAS_AS_COMPETENCIAS):
        print(f"  [{i+1}] {competencia.nome} ({competencia.tipo})")
    print("-" * 40)

def cadastrar_perfil() -> Perfil:
    """
    Cria um novo perfil de usuário, solicitando nome e competências.
    """
    nome = input("Digite o seu nome: ")
    perfil_usuario = Perfil(nome_usuario=nome)
    
    while True:
        exibir_menu_competencias()
        escolha = input("Suas escolhas (ex: 1, 4, 7): ")
        
        try:
            # Processa os números digitados
            indices_escolhidos = [int(i.strip()) for i in escolha.split(',')]
            
            competencias_selecionadas = set()
            for i in indices_escolhidos:
                if 1 <= i <= len(TODAS_AS_COMPETENCIAS):
                    competencias_selecionadas.add(TODAS_AS_COMPETENCIAS[i-1])
                else:
                    print(f"Opção {i} é inválida e será ignorada.")
            
            perfil_usuario.competencias_usuario = competencias_selecionadas
            print(f"\nPerfil de {nome} atualizado com {len(competencias_selecionadas)} competências!")
            break
        except ValueError:
            print("\n*** Erro: Por favor, digite apenas números separados por vírgula. ***")
        except Exception as e:
            print(f"\n*** Ocorreu um erro: {e} ***")
            
    return perfil_usuario

def mostrar_recomendacoes(perfil: Perfil):
    """
    Busca e exibe as recomendações de carreira para o perfil.
    """
    if not perfil:
        print("\n*** Você precisa cadastrar um perfil primeiro! (Opção 1) ***")
        return

    print(f"\nGerando recomendações para {perfil.nome_usuario}...")
    time.sleep(1) # Simula processamento
    
    recomendacoes = gerar_recomendacoes(perfil, LISTA_DE_CARREIRAS)

    if not recomendacoes:
        print("\nNenhuma carreira compatível encontrada com seu perfil atual.")
        print("Tente adicionar mais competências!")
        return

    print("\n--- 🚀 Recomendações de Carreira para Você ---")
    for r in recomendacoes:
        carreira = r['carreira']
        print(f"\n--- {carreira.nome} --- ({r['percentual_match']:.0f}% compatível)")
        print(f"  Descrição: {carreira.descricao}")
        
        # Mostra as competências que faltam (Trilha de aprendizado) [cite: 9]
        if r['competencias_faltantes']:
            print("  🎯 Áreas para Aprimoramento:")
            for c in r['competencias_faltantes']:
                print(f"     - {c.nome}")
        else:
            print("  ✅ Você tem todas as competências para esta carreira!")
    print("-" * 40)


def main():
    """Função principal que executa o menu da CLI."""
    print("========================================")
    print("  Bem-vindo ao Future at Work")
    print("  Sistema de Orientação de Carreiras")
    print("========================================")
    
    perfil_ativo = None

    while True:
        print("\n--- Menu Principal ---")
        print("[1] Cadastrar / Atualizar Perfil e Competências")
        print("[2] Ver Recomendações de Carreira")
        print("[3] Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            perfil_ativo = cadastrar_perfil()
        elif opcao == '2':
            mostrar_recomendacoes(perfil_ativo)
        elif opcao == '3':
            print("\nObrigado por usar o sistema. O futuro espera por você!")
            break
        else:
            print("\n*** Opção inválida! Tente novamente. ***")

# Ponto de entrada do script
if __name__ == "__main__":
    main()