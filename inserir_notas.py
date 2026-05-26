from cadastro_aluno import alunos
from cadastro_disciplina import encontrar_disciplina

historico_academico = []

def inserir_notas():
    print("\n=== INSERIR NOTAS ===")

    try:
        RA_aluno = int(input("Digite o RA do aluno: "))
    except ValueError:
        print("RA inválido.")
        return

    if RA_aluno not in alunos:
        print("Aluno não encontrado.")
        return

    id_disciplina = input("Digite o código da disciplina: ")

    disc = encontrar_disciplina(id_disciplina)
    if not disc:
        print("Disciplina não encontrada.")
        return

    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
    except ValueError:
        print("Notas inválidas.")
        return

    media = (nota1 + nota2) / 2

    semestre = input("Digite o semestre (ex: 2026.1): ")

    registro = {
        "RA_aluno": RA_aluno,
        "id_disciplina": id_disciplina,
        "nota": media,
        "semestre": semestre
    }

    historico_academico.append(registro)

    print(f"\nNotas registradas com sucesso em {disc['nome']}!\n")