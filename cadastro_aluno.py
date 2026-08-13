# ============================================================
# BRANCH: Cadastro aluno
# RESPONSÁVEL: Pedro Henrique
# DESCRIÇÃO: Módulo para cadastro e listagem de alunos
# ============================================================

import json
import os
from validacoes import validar_nome, validar_matricula
from typing import Optional

ARQUIVO_ALUNOS = "dados/alunos.json"

def _carregar_alunos() -> dict:
    """Carrega os alunos salvos no arquivo JSON."""
    if not os.path.exists(ARQUIVO_ALUNOS):
        return {}
    with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as f:
        return json.load(f)

def _salvar_alunos(alunos: dict) -> None:
    """Salva os alunos no arquivo JSON."""
    os.makedirs("dados", exist_ok=True)
    with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as f:
        json.dump(alunos, f, ensure_ascii=False, indent=4)

def cadastrar_aluno() -> None:
    """Realiza o cadastro de um novo aluno."""
    print("=" * 45)
    print("        CADASTRO DE ALUNO")
    print("=" * 45)

    matricula = input("Digite a matrícula do aluno: ").strip()
    if not validar_matricula(matricula):
        print("[!] Matrícula inválida. Use apenas números (mín. 4 dígitos).")
        return

    alunos = _carregar_alunos()

    if matricula in alunos:
        print(f"[!] Matrícula {matricula} já cadastrada.")
        return

    nome = input("Digite o nome completo do aluno: ").strip()
    if not validar_nome(nome):
        print("[!] Nome inválido. Use apenas letras e espaços (mín. 3 caracteres).")
        return

    curso = input("Digite o curso do aluno: ").strip()
    if not curso:
        print("[!] Curso não pode ser vazio.")
        return

    alunos[matricula] = {
        "nome": nome,
        "curso": curso,
        "notas": {}
    }

    _salvar_alunos(alunos)
    print(f"\n✅ Aluno '{nome}' cadastrado com sucesso! Matrícula: {matricula}")

def listar_alunos() -> None:
    """Lista todos os alunos cadastrados."""
    print("=" * 45)
    print("         ALUNOS CADASTRADOS")
    print("=" * 45)

    alunos = _carregar_alunos()

    if not alunos:
        print("[!] Nenhum aluno cadastrado.")
        return

    for matricula, dados in alunos.items():
        print(f"\n  Matrícula : {matricula}")
        print(f"  Nome      : {dados['nome']}")
        print(f"  Curso     : {dados['curso']}")
        print("-" * 45)

def buscar_aluno(matricula: str) -> Optional[dict]:
    """Busca e retorna os dados de um aluno pela matrícula."""
    alunos = _carregar_alunos()
    return alunos.get(matricula, None)

def atualizar_aluno(matricula: str, dados: dict) -> None:
    """Atualiza os dados de um aluno existente."""
    alunos = _carregar_alunos()
    if matricula in alunos:
        alunos[matricula] = dados
        _salvar_alunos(alunos)
