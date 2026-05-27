# ============================================================
# BRANCH: Cadastro disciplina
# RESPONSÁVEL: Richard Sieber
# DESCRIÇÃO: Módulo para cadastro e listagem de disciplinas
# ============================================================

import json
import os
from typing import Optional
from validacoes import validar_nome

ARQUIVO_DISCIPLINAS = "dados/disciplinas.json"

def _carregar_disciplinas() -> dict:
    """Carrega as disciplinas salvas no arquivo JSON."""
    if not os.path.exists(ARQUIVO_DISCIPLINAS):
        return {}
    with open(ARQUIVO_DISCIPLINAS, "r", encoding="utf-8") as f:
        return json.load(f)

def _salvar_disciplinas(disciplinas: dict) -> None:
    """Salva as disciplinas no arquivo JSON."""
    os.makedirs("dados", exist_ok=True)
    with open(ARQUIVO_DISCIPLINAS, "w", encoding="utf-8") as f:
        json.dump(disciplinas, f, ensure_ascii=False, indent=4)

def cadastrar_disciplina() -> None:
    """Realiza o cadastro de uma nova disciplina."""
    print("=" * 45)
    print("       CADASTRO DE DISCIPLINA")
    print("=" * 45)

    codigo = input("Digite o código da disciplina (ex: MAT01): ").strip().upper()
    if not codigo or len(codigo) < 3:
        print("[!] Código inválido. Mínimo de 3 caracteres.")
        return

    disciplinas = _carregar_disciplinas()

    if codigo in disciplinas:
        print(f"[!] Disciplina com código '{codigo}' já cadastrada.")
        return

    nome = input("Digite o nome da disciplina: ").strip()
    if not validar_nome(nome):
        print("[!] Nome inválido. Use apenas letras e espaços (mín. 3 caracteres).")
        return

    carga_str = input("Digite a carga horária (horas): ").strip()
    if not carga_str.isdigit() or int(carga_str) <= 0:
        print("[!] Carga horária inválida.")
        return

    disciplinas[codigo] = {
        "nome": nome,
        "carga_horaria": int(carga_str)
    }

    _salvar_disciplinas(disciplinas)
    print(f"\n✅ Disciplina '{nome}' cadastrada com sucesso! Código: {codigo}")

def listar_disciplinas() -> None:
    """Lista todas as disciplinas cadastradas."""
    print("=" * 45)
    print("      DISCIPLINAS CADASTRADAS")
    print("=" * 45)

    disciplinas = _carregar_disciplinas()

    if not disciplinas:
        print("[!] Nenhuma disciplina cadastrada.")
        return

    for codigo, dados in disciplinas.items():
        print(f"\n  Código         : {codigo}")
        print(f"  Nome           : {dados['nome']}")
        print(f"  Carga Horária  : {dados['carga_horaria']}h")
        print("-" * 45)

def buscar_disciplina(codigo: str) -> Optional[dict]:
    """Busca e retorna os dados de uma disciplina pelo código."""
    disciplinas = _carregar_disciplinas()
    return disciplinas.get(codigo.upper(), None)
