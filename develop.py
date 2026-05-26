from cadastro_aluno import *
from cadastro_disciplina import inserir_disciplina, banco_disciplinas
from inserir_notas import *
from calculo_media import *
from historico_aluno import *

while True:
    print("\n====== MENU ======")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Cadastrar disciplina")
    print("4 - Inserir notas")
    print("5 - Calcular média")
    print("6 - Histórico do aluno")
    print("0 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        cadastrar_aluno()

    elif op == "2":
        listar_alunos()

    elif op == "3":
        inserir_disciplina()

    elif op == "4":
        inserir_notas()

    elif op == "5":
        calcular_media()

    elif op == "6":
        exibir_historico_aluno()

    elif op == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida")