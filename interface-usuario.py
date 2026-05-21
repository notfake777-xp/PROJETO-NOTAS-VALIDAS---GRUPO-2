============================================================
# BRANCH: feature/interface-usuario
# RESPONSÁVEL: Gabriel Soares
# DESCRIÇÃO: Arquivo principal da interface do usuário
# ============================================================

from cadastro_aluno import cadastrar_aluno
from cadastro_disciplina import cadastrar_disciplina
from inserir_notas import inserir_notas
from calculo_media import calcular_media
from situacao_aluno import verificar_situacao
from historico_aluno import mostrar_historico


def limpar_tela():
    print("\n" * 40)


def pausar():
    input("\nPressione ENTER para continuar...")


def menu_principal():

    while True:
        limpar_tela()

        print("=" * 50)
        print("      SISTEMA DE REGISTRO DE NOTAS")
        print("=" * 50)
        print("1 - Cadastro de alunos")
        print("2 - Cadastro de disciplinas")
        print("3 - Inserir notas")
        print("4 - Calcular média do aluno")
        print("5 - Verificar situação do aluno")
        print("6 - Histórico acadêmico")
        print("0 - Sair")
        print("=" * 50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            print("=== CADASTRO DE ALUNOS ===\n")

            try:
                cadastrar_aluno()
            except Exception as erro:
                print(f"Erro ao cadastrar aluno: {erro}")

            pausar()

        elif opcao == "2":
            limpar_tela()
            print("=== CADASTRO DE DISCIPLINAS ===\n")

            try:
                cadastrar_disciplina()
            except Exception as erro:
                print(f"Erro ao cadastrar disciplina: {erro}")

            pausar()

        elif opcao == "3":
            limpar_tela()
            print("=== INSERÇÃO DE NOTAS ===\n")

            try:
                inserir_notas()
            except Exception as erro:
                print(f"Erro ao inserir notas: {erro}")

            pausar()

        elif opcao == "4":
            limpar_tela()
            print("=== CÁLCULO DE MÉDIA ===\n")

            try:
                calcular_media()
            except Exception as erro:
                print(f"Erro ao calcular média: {erro}")

            pausar()

        elif opcao == "5":
            limpar_tela()
            print("=== SITUAÇÃO DO ALUNO ===\n")

            try:
                verificar_situacao()
            except Exception as erro:
                print(f"Erro ao verificar situação: {erro}")

            pausar()

        elif opcao == "6":
            limpar_tela()
            print("=== HISTÓRICO ACADÊMICO ===\n")

            try:
                mostrar_historico()
            except Exception as erro:
                print(f"Erro ao exibir histórico: {erro}")

            pausar()

        elif opcao == "0":
            limpar_tela()
            print("Encerrando o sistema...")
            print("Obrigado por utilizar o Registro de Notas!")
            break

        else:
            print("\nOpção inválida!")
            pausar()


if __name__ == "__main__":
    menu_principal()