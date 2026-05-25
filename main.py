# ============================================================
# BRANCH: main
# RESPONSÁVEL: Salatiel
# DESCRIÇÃO: Arquivo principal do sistema de registro de notas
# ============================================================

from cadastro_aluno import cadastrar_aluno, listar_alunos
from cadastro_disciplina import cadastrar_disciplina, listar_disciplinas
from inserir_notas import inserir_nota
from calculo_media import calcular_media
from situacao_aluno import Situação_aluno_calculadora
from historico_aluno import exibir_historico
from interface_usuario import exibir_menu, obter_opcao, limpar_tela, exibir_cabecalho
from validacoes import validar_opcao_menu

def main():
    """Função principal que orquestra o sistema."""
    while True:
        limpar_tela()
        exibir_cabecalho()
        exibir_menu()
        
        opcao_str = obter_opcao()
        
        if not validar_opcao_menu(opcao_str, 1, 8):
            input("\n[!] Opção inválida. Pressione Enter para continuar...")
            continue
        
        opcao = int(opcao_str)

        if opcao == 1:
            limpar_tela()
            cadastrar_aluno()
            input("\nPressione Enter para continuar...")

        elif opcao == 2:
            limpar_tela()
            cadastrar_disciplina()
            input("\nPressione Enter para continuar...")

        elif opcao == 3:
            limpar_tela()
            listar_alunos()
            input("\nPressione Enter para continuar...")

        elif opcao == 4:
            limpar_tela()
            inserir_nota()
            input("\nPressione Enter para continuar...")

        elif opcao == 5:
            limpar_tela()
            calcular_media()
            input("\nPressione Enter para continuar...")

        elif opcao == 6:
            limpar_tela()
            verificar_situacao()
            input("\nPressione Enter para continuar...")

        elif opcao == 7:
            limpar_tela()
            exibir_historico()
            input("\nPressione Enter para continuar...")

        elif opcao == 8:
            print("\n✅ Sistema encerrado. Até logo!\n")
            break

if __name__ == "__main__":
    main()
