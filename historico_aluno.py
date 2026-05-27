# ============================================================
# BRANCH: Histórico aluno
# RESPONSÁVEL: Anderson
# DESCRIÇÃO: Módulo para exibição e salvamento do histórico
# ============================================================

import json
import os
from datetime import datetime
from cadastro_aluno import buscar_aluno
from calculo_media import obter_media_aluno
from cadastro_disciplina import buscar_disciplina

ARQUIVO_HISTORICO = "dados/historico.json"

def _carregar_historico() -> dict:
    if not os.path.exists(ARQUIVO_HISTORICO):
        return {}
    with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
        return json.load(f)

def _salvar_historico(historico: dict) -> None:
    os.makedirs("dados", exist_ok=True)
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=4)

def exibir_historico() -> None:
    """Exibe e salva o histórico acadêmico de um aluno."""
    print("=" * 50)
    print("        HISTÓRICO DO ALUNO")
    print("=" * 50)

    matricula = input("Digite a matrícula do aluno: ").strip()
    aluno = buscar_aluno(matricula)

    if aluno is None:
        print(f"[!] Aluno com matrícula '{matricula}' não encontrado.")
        return

    medias = obter_media_aluno(matricula)

    if not medias:
        print("[!] Nenhuma nota registrada para este aluno.")
        return

    data_consulta = datetime.now().strftime("%d/%m/%Y %H:%M")

    print(f"\n  Aluno     : {aluno['nome']}")
    print(f"  Matrícula : {matricula}")
    print(f"  Curso     : {aluno['curso']}")
    print(f"  Gerado em : {data_consulta}")
    print("\n" + "-" * 50)
    print(f"  {'DISCIPLINA':<22} {'MÉDIA':>6}   STATUS")
    print("-" * 50)

    registro_historico = []

    for codigo, info in medias.items():
        disciplina = buscar_disciplina(codigo)
        nome_disc = disciplina["nome"] if disciplina else codigo
        print(f"  {nome_disc:<22} {info['media']:>6.2f}   {info['status']}")

        registro_historico.append({
            "codigo": codigo,
            "disciplina": nome_disc,
            "media": info["media"],
            "status": info["status"]
        })

    print("=" * 50)

    # Salvar histórico automaticamente
    historico = _carregar_historico()
    if matricula not in historico:
        historico[matricula] = []

    historico[matricula].append({
        "data": data_consulta,
        "nome": aluno["nome"],
        "curso": aluno["curso"],
        "disciplinas": registro_historico
    })

    _salvar_historico(historico)
    print(f"\n✅ Histórico salvo automaticamente em '{ARQUIVO_HISTORICO}'.")

def consultar_historico_completo() -> None:
    """Exibe todo o histórico de consultas de um aluno."""
    print("=" * 50)
    print("     HISTÓRICO COMPLETO DE CONSULTAS")
    print("=" * 50)

    matricula = input("Digite a matrícula do aluno: ").strip()
    historico = _carregar_historico()

    if matricula not in historico or not historico[matricula]:
        print("[!] Nenhum histórico encontrado para esta matrícula.")
        return

    for i, registro in enumerate(historico[matricula], 1):
        print(f"\n  [{i}] Consulta em: {registro['data']}")
        print(f"      Aluno: {registro['nome']} | Curso: {registro['curso']}")
        for disc in registro["disciplinas"]:
            print(f"      - {disc['disciplina']:<20} Média: {disc['media']:.2f}  {disc['status']}")
