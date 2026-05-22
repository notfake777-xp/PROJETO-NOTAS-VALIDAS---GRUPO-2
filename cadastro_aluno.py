alunos = []

def cadastrar_aluno():
    print("\n=== CADASTRO DE ALUNO ===")

    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula: ")
    turma = input("Digite a turma: ")

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "turma": turma
    }

    alunos.append(aluno)

    print("\nAluno cadastrado com sucesso!\n")


def listar_alunos():

    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado.\n")
        return

    print("\n=== LISTA DE ALUNOS ===")

    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Turma: {aluno['turma']}")
        print("------------------------")


while True:

    print("====== MENU ======")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida!\n")