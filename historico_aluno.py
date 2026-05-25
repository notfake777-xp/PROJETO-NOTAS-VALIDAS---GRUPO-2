# historico_aluno.py

# --- IMPORTS --- #
from cadastro_aluno import alunos
from cadastro_disciplina import encontrar_disciplina
from inserir_notas import historico_academico


# --- FUNÇÕES --- #

def verificar_situacao(nota: float, media_aprovacao: float = 7.0) -> str:
    if nota >= media_aprovacao:
        return "Aprovado"
    else:
        return "Reprovado"


def registrar_nota(RA_aluno: int, id_disciplina: str, semestre: str, nota: float):
    if RA_aluno not in alunos:
        print(f"Erro: Aluno com RA {RA_aluno} não encontrado.")
        return

    disc = encontrar_disciplina(id_disciplina)
    if not disc:
        print(f"Erro: Disciplina com ID {id_disciplina} não encontrada.")
        return

    if not (0 <= nota <= 10):
        print("Erro: A nota deve estar entre 0 e 10.")
        return

    # Verifica se já existe registro
    for registro in historico_academico:
        if (
            registro['RA_aluno'] == RA_aluno and
            registro['id_disciplina'] == id_disciplina and
            registro['semestre'] == semestre
        ):
            registro['nota'] = nota
            print(f"Nota atualizada para {nota} em {disc['nome']}.")
            return

    # Novo registro
    historico_academico.append({
        'RA_aluno': RA_aluno,
        'id_disciplina': id_disciplina,
        'semestre': semestre,
        'nota': nota
    })

    print(f"Nota {nota} registrada para {alunos[RA_aluno]['nome']} em {disc['nome']}.")


def obter_historico_aluno(RA_aluno: int):
    if RA_aluno not in alunos:
        print(f"Erro: Aluno com RA {RA_aluno} não encontrado.")
        return []

    return [
        registro for registro in historico_academico
        if registro['RA_aluno'] == RA_aluno
    ]


def exibir_historico_aluno():
    print("\n--- HISTÓRICO DO ALUNO ---")

    try:
        RA_aluno = int(input("Digite o RA do aluno: "))
    except ValueError:
        print("Erro: RA deve ser um número.")
        return

    if RA_aluno not in alunos:
        print("Aluno não encontrado.")
        return

    aluno_nome = alunos[RA_aluno]['nome']
    historico = obter_historico_aluno(RA_aluno)

    if not historico:
        print("Nenhum histórico encontrado.")
        return

    print(f"\n=== Histórico de {aluno_nome} ({RA_aluno}) ===")

    # Agrupar por semestre
    historico_por_semestre = {}

    for registro in historico:
        semestre = registro['semestre']
        historico_por_semestre.setdefault(semestre, []).append(registro)

    for semestre in sorted(historico_por_semestre):
        print(f"\nSemestre: {semestre}")

        for registro in historico_por_semestre[semestre]:
            disc = encontrar_disciplina(registro['id_disciplina'])
            nome_disc = disc['nome'] if disc else "Desconhecida"

            nota = registro['nota']
            situacao = verificar_situacao(nota)

            print(f"- {nome_disc} ({registro['id_disciplina']}) | Nota: {nota:.2f} | {situacao}")

    print("\n----------------------------")