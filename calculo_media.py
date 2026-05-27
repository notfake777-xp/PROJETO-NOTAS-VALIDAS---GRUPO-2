# ============================================================
# BRANCH: Calculo media
# RESPONSÁVEL: Rinaldo Neto
# DESCRIÇÃO: Módulo para cálculo de médias por disciplina
# ============================================================

from cadastro_aluno import buscar_aluno
from cadastro_disciplina import buscar_disciplina

NOTA_MINIMA_APROVACAO = 6.0
NOTA_RECUPERACAO = 4.0

def _calcular_media_disciplina(notas: dict) -> float:
    """Calcula a média aritmética simples das notas de uma disciplina."""
    valores = [notas.get(f"nota{i}", 0.0) for i in range(1, 4)]
    return round(sum(valores) / len(valores), 2)

def calcular_media() -> None:
    """Exibe as médias de todas as disciplinas de um aluno."""
    print("=" * 45)
    print("         CÁLCULO DE MÉDIAS")
    print("=" * 45)

    matricula = input("Digite a matrícula do aluno: ").strip()
    aluno = buscar_aluno(matricula)

    if aluno is None:
        print(f"[!] Aluno com matrícula '{matricula}' não encontrado.")
        return

    print(f"\n  Aluno : {aluno['nome']}")
    print(f"  Curso : {aluno['curso']}")

    notas_aluno = aluno.get("notas", {})

    if not notas_aluno:
        print("\n[!] Nenhuma nota registrada para este aluno.")
        return

    print("\n" + "=" * 45)
    print(f"  {'DISCIPLINA':<20} {'MÉDIA':>6}  {'STATUS'}")
    print("=" * 45)

    for codigo, notas in notas_aluno.items():
        disciplina = buscar_disciplina(codigo)
        nome_disc = disciplina["nome"] if disciplina else codigo

        media = _calcular_media_disciplina(notas)
        status = _definir_status(media)

        print(f"  {nome_disc:<20} {media:>6.2f}   {status}")

    print("=" * 45)

def obter_media_aluno(matricula: str) -> dict:
    """
    Retorna um dicionário com as médias por disciplina de um aluno.
    Usado por outros módulos (situacao, historico).
    """
    aluno = buscar_aluno(matricula)
    if aluno is None:
        return {}

    resultado = {}
    for codigo, notas in aluno.get("notas", {}).items():
        media = _calcular_media_disciplina(notas)
        status = _definir_status(media)
        resultado[codigo] = {"media": media, "status": status}

    return resultado

def _definir_status(media: float) -> str:
    """Define o status do aluno com base na média."""
    if media >= NOTA_MINIMA_APROVACAO:
        return "✅ Aprovado"
    elif media >= NOTA_RECUPERACAO:
        return "⚠️  Recuperação"
    else:
        return "❌ Reprovado"
