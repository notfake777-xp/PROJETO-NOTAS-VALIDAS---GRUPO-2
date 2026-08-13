# ============================================================
# BRANCH: Interface usuário
# RESPONSÁVEL: Gabriel Soares
# DESCRIÇÃO: Módulo responsável pela interface do terminal
# ============================================================

import os
import platform

def limpar_tela() -> None:
    """Limpa o terminal de acordo com o sistema operacional."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def exibir_cabecalho() -> None:
    """Exibe o cabeçalho visual do sistema."""
    print("=" * 50)
    print("      SISTEMA DE REGISTRO DE NOTAS")
    print("        Projeto Acadêmico - 2026")
    print("=" * 50)

def exibir_menu() -> None:
    """Exibe o menu principal de opções."""
    print("\n  Selecione uma opção:\n")
    print("  [1] Cadastrar Aluno")
    print("  [2] Cadastrar Disciplina")
    print("  [3] Listar Alunos")
    print("  [4] Inserir Notas")
    print("  [5] Calcular Médias")
    print("  [6] Situação do Aluno")
    print("  [7] Histórico do Aluno")
    print("  [8] Sair")
    print("\n" + "-" * 50)

def obter_opcao() -> str:
    """Lê e retorna a opção digitada pelo usuário."""
    return input("  Opção: ").strip()

def exibir_mensagem_sucesso(mensagem: str) -> None:
    """Exibe uma mensagem de sucesso formatada."""
    print(f"\n  ✅ {mensagem}")

def exibir_mensagem_erro(mensagem: str) -> None:
    """Exibe uma mensagem de erro formatada."""
    print(f"\n  ❌ {mensagem}")

def exibir_mensagem_aviso(mensagem: str) -> None:
    """Exibe uma mensagem de aviso formatada."""
    print(f"\n  ⚠️  {mensagem}")

def exibir_separador(caractere: str = "-", tamanho: int = 50) -> None:
    """Exibe uma linha separadora."""
    print(caractere * tamanho)

def exibir_titulo_secao(titulo: str) -> None:
    """Exibe um título de seção centralizado."""
    print("=" * 50)
    print(f"  {titulo.upper()}")
    print("=" * 50)

def confirmar_acao(mensagem: str) -> bool:
    """Solicita confirmação do usuário para uma ação."""
    resposta = input(f"\n  {mensagem} (s/n): ").strip().lower()
    return resposta == "s"
