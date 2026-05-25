alunos = {}

def cadastrar_aluno():
    print("\n=== CADASTRO DE ALUNO ===")

    try:
        RA_aluno = int(input("Digite o RA do aluno: "))
    except ValueError:
        print("Erro: RA deve ser número.")
        return

    if RA_aluno in alunos:
        print("Erro: RA já cadastrado.")
        return

    nome = input("Digite o nome do aluno: ")
    turma = input("Digite a turma: ")

    alunos[RA_aluno] = {
        "nome": nome,
        "turma": turma
    }

    print("\nAluno cadastrado com sucesso!\n")


def listar_alunos():

    if not alunos:
        print("\nNenhum aluno cadastrado.\n")
        return

    print("\n=== LISTA DE ALUNOS ===")

    for RA_aluno, dados in alunos.items():
        print(f"RA: {RA_aluno}")
        print(f"Nome: {dados['nome']}")
        print(f"Turma: {dados['turma']}")
        print("------------------------")