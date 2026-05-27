# ============================================================
# BRANCH: Inserir notas
# RESPONSÁVEL: Felipe Farias
# DESCRIÇÃO: Módulo para inserção de notas por disciplina
# ============================================================

from cadastro_aluno import buscar_aluno, atualizar_aluno
from cadastro_disciplina import buscar_disciplina, listar_disciplinas
from validacoes import validar_nota

def inserir_nota() -> None:
    """Insere ou atualiza a nota de um aluno em uma disciplina."""
    print("=" * 45)
    print("          INSERIR NOTA")
    print("=" * 45)

    matricula = input("Digite a matrícula do aluno: ").strip()
    aluno = buscar_aluno(matricula)

    if aluno is None:
        print(f"[!] Aluno com matrícula '{matricula}' não encontrado.")
        return

    print(f"\n  Aluno encontrado: {aluno['nome']} | Curso: {aluno['curso']}")

    print("\nDisciplinas disponíveis:")
    listar_disciplinas()

    codigo = input("Digite o código da disciplina: ").strip().upper()
    disciplina = buscar_disciplina(codigo)

    if disciplina is None:
        print(f"[!] Disciplina '{codigo}' não encontrada.")
        return

    print(f"\n  Disciplina: {disciplina['nome']}")
    print("  Informe as notas (0.0 a 10.0):\n")

    notas_inseridas = {}

    for i in range(1, 4):
        while True:
            nota_str = input(f"  Nota {i}: ").strip().replace(",", ".")
            if validar_nota(nota_str):
                notas_inseridas[f"nota{i}"] = float(nota_str)
                break
            else:
                print("  [!] Nota inválida. Digite um valor entre 0.0 e 10.0.")

    # Verifica se já existe registro para a disciplina
    if codigo in aluno["notas"]:
        sobrescrever = input(
            f"\n  [!] Já existem notas para '{disciplina['nome']}'. Deseja substituir? (s/n): "
        ).strip().lower()
        if sobrescrever != "s":
            print("  [!] Operação cancelada.")
            return

    aluno["notas"][codigo] = notas_inseridas
    atualizar_aluno(matricula, aluno)

    print(f"\n✅ Notas da disciplina '{disciplina['nome']}' salvas com sucesso!")
    print(f"   Nota 1: {notas_inseridas['nota1']} | Nota 2: {notas_inseridas['nota2']} | Nota 3: {notas_inseridas['nota3']}")
