# Versão 2.0 do meu código do histórico de notas
import json

# --- Estruturas de Dados --- #

# Dicionário para armazenar informações dos alunos
# Exemplo: {12345: {'nome': 'Nome do Aluno'}}
alunos = {}

# Dicionário para armazenar informações das disciplinas
# Exemplo: {'disc_id': {'nome': 'Nome da Disciplina', 'creditos': 4}}
disciplinas = {}

# Lista para armazenar o histórico acadêmico
# Cada item é um dicionário representando uma nota de um aluno em uma disciplina num semestre
historico_academico = []
# Dicionário para armazenar informações do aluno
alunos = { 
# Exemplo: 'aluno_RA': {'nome': 'Nome do Aluno'}
}

# Dicionário para armazenar informações das disciplinas
disciplinas = {
    # Exemplo: 'disc_id': {'nome': 'Nome da Disciplina', 'creditos': 4}
}

# Lista para armazenar o histórico acadêmico
# Cada item é um dicionário representando uma nota de um aluno em uma disciplina num semestre
historico_academico = [alunos, disciplinas]


# --- Funções de Gerenciamento --- #

def adicionar_aluno(RA_aluno: int, nome_aluno: str):
    # Adiciona um novo aluno ao sistema
    if RA_aluno in alunos:
        print(f"{nome_aluno} com ID {RA_aluno} já existe.")
    else:
        alunos[RA_aluno] = {'nome': nome_aluno}
        print(f"Aluno {nome_aluno} com ({RA_aluno}) adicionado com sucesso.")

def adicionar_disciplina(id_disciplina: str, nome_disciplina: str, creditos: int):
    # Adiciona uma nova disciplina ao sistema.
    if id_disciplina in disciplinas:
        print(f"Disciplina com ID {id_disciplina} já existe.")
    else:
        disciplinas[id_disciplina] = {'nome': nome_disciplina, 'creditos': creditos}
        print(f"Disciplina {nome_disciplina} com ({id_disciplina}) adicionada com sucesso.")

def registrar_nota(RA_aluno: int, id_disciplina: str, semestre: float, nota: float):
    # Registra uma nota para um aluno em uma disciplina e semestre específicos.
    if RA_aluno not in alunos:
        print(f"Erro: Aluno com ID {RA_aluno} não encontrado.")
        return input(f"Digite o RA do aluno manualmente: ")
    if id_disciplina not in disciplinas:
        print(f"Erro: Disciplina com ID {id_disciplina} não encontrada.")
        return input(f"Digite o ID da disciplina manualmente: ")
    if not (0 <= nota <= 10):
        print("Erro: A nota deve estar entre 0 e 10.")
        return input(f'Digite a nota manualmente: ')

    # Verifica se já existe um registro para este aluno, disciplina e semestre
    resgistro_aluno = registro in historico_academico
    for registro in historico_academico:
        if (registro['RA_aluno'] == RA_aluno and
            registro['id_disciplina'] == id_disciplina and
            registro['semestre'] == semestre):
            registro['nota'] = nota  # Atualiza a nota se já existir
            print(f"Nota do aluno {alunos[RA_aluno]['nome']} em {disciplinas[id_disciplina]['nome']} no {semestre} atualizada para {nota}.")
            return

    # Adiciona um novo registro de nota
    historico_academico.append({
        'RA_aluno': RA_aluno,
        'id_disciplina': id_disciplina,
        'semestre': semestre,
        'nota': nota
    })
    print(f"Nota {nota} registrada para {alunos[RA_aluno]['nome']} em {disciplinas[id_disciplina]['nome']} no {semestre}.")

def verificar_situacao(nota: float, media_aprovacao: float = 7.0) -> str:
    # Verifica a situação do aluno (Aprovado/Reprovado) com base na nota.
    if nota >= media_aprovacao:
        return "Aprovado"
    else:
        return "Reprovado"

def obter_historico_aluno(RA_aluno: int) -> list:
    # Retorna uma lista de registros de notas de um aluno.
    if RA_aluno not in alunos:
        print(f"Erro: Aluno com RA {RA_aluno} não encontrado.")
        return []
    return [registro for registro in historico_academico if registro['RA_aluno'] == RA_aluno]

def exibir_historico_aluno(RA_aluno: int, media_aprovacao: float = 7.0):
    # Exibe o histórico acadêmico detalhado de um aluno.
    if RA_aluno not in alunos:
        print(f"Erro: Aluno com RA {RA_aluno} não encontrado.")
        return

    aluno_nome = alunos[RA_aluno]['nome']
    print(f"\n--- Histórico Acadêmico de: {aluno_nome} ({RA_aluno}) ---")

    historico = obter_historico_aluno(RA_aluno)

    if not historico:
        print("Nenhum registro de nota encontrado para este aluno.")
        return

    # Agrupar por semestre para uma melhor visualização
    historico_por_semestre = {}
    for registro in historico:
        semestre = registro['semestre']
        if semestre not in historico_por_semestre:
            historico_por_semestre[semestre] = []
        historico_por_semestre[semestre].append(registro)

    for semestre, registros_do_semestre in sorted(historico_por_semestre.items()):
        print(f"\n  Semestre: {semestre}")
        for registro in registros_do_semestre:
            disciplina_id = registro['id_disciplina']
            disciplina_nome = disciplinas.get(disciplina_id, {'nome': 'Desconhecida'})['nome']
            nota = registro['nota']
            situacao = verificar_situacao(nota, media_aprovacao)
            print(f"    - Disciplina: {disciplina_nome} ({disciplina_id}) | Nota: {nota:.2f} | Situação: {situacao}")

    print("--------------------------------------------------")
