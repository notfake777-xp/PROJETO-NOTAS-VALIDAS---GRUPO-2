# ============================================================
# BRANCH: Situação aluno
# RESPONSÁVEL: Daniel
# DESCRIÇÃO: Módulo para verificar a situação geral do aluno
# ============================================================

from cadastro_aluno import buscar_aluno
from calculo_media import obter_media_aluno
from cadastro_disciplina import buscar_disciplina

def verificar_situacao() -> None:
    """Exibe a situação completa de um aluno em todas as disciplinas."""
    print("=" * 50)
    print("        SITUAÇÃO DO ALUNO")
    print("=" * 50)

    matricula = input("Digite a matrícula do aluno: ").strip()
    aluno = buscar_aluno(matricula)

    if aluno is None:
        print(f"[!] Aluno com matrícula '{matricula}' não encontrado.")
        return

    medias = obter_media_aluno(matricula)

    if not medias:
        print(f"\n  Aluno: {aluno['nome']}")
        print("[!] Nenhuma nota registrada. Situação indefinida.")
        return

    total = len(medias)
    aprovados = sum(1 for d in medias.values() if d["status"].startswith("✅"))
    recuperacao = sum(1 for d in medias.values() if d["status"].startswith("⚠️"))
    reprovados = sum(1 for d in medias.values() if d["status"].startswith("❌"))

    print(f"\n  Aluno      : {aluno['nome']}")
    print(f"  Matrícula  : {matricula}")
    print(f"  Curso      : {aluno['curso']}")
    print("\n" + "-" * 50)
    print(f"  {'DISCIPLINA':<22} {'MÉDIA':>6}   STATUS")
    print("-" * 50)

    for codigo, info in medias.items():
        disciplina = buscar_disciplina(codigo)
        nome_disc = disciplina["nome"] if disciplina else codigo
        print(f"  {nome_disc:<22} {info['media']:>6.2f}   {info['status']}")

    print("=" * 50)
    print(f"\n  RESUMO GERAL:")
    print(f"  Total de disciplinas : {total}")
    print(f"  Aprovadas            : {aprovados}")
    print(f"  Em recuperação       : {recuperacao}")
    print(f"  Reprovadas           : {reprovados}")
    print("\n" + "=" * 50)

    situacao_geral = _calcular_situacao_geral(aprovados, recuperacao, reprovados, total)
    print(f"  SITUAÇÃO GERAL: {situacao_geral}")
    print("=" * 50)

def _calcular_situacao_geral(aprovados: int, recuperacao: int, reprovados: int, total: int) -> str:
    """Determina a situação geral do aluno no semestre."""
    if reprovados == 0 and recuperacao == 0:
        return "🎓 APROVADO EM TODAS AS DISCIPLINAS"
    elif reprovados > total // 2:
        return "❌ REPROVADO NO SEMESTRE"
    elif recuperacao > 0 or reprovados > 0:
        return "⚠️  EM RECUPERAÇÃO / SITUAÇÃO PENDENTE"
    else:
        return "✅ APROVADO"
