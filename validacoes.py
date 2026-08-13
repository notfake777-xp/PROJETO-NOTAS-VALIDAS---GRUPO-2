# ============================================================
# BRANCH: validações
# RESPONSÁVEL: Iago 
# DESCRIÇÃO: Módulo com todas as funções de validação do sistema
# ============================================================

import re

def validar_nota(valor: str) -> bool:
    """
    Verifica se o valor é uma nota válida entre 0.0 e 10.0.
    Aceita vírgula ou ponto como separador decimal.
    """
    try:
        nota = float(valor.replace(",", "."))
        return 0.0 <= nota <= 10.0
    except ValueError:
        return False

def validar_matricula(matricula: str) -> bool:
    """
    Verifica se a matrícula é válida.
    Deve conter apenas dígitos e ter no mínimo 4 caracteres.
    """
    return matricula.isdigit() and len(matricula) >= 4

def validar_nome(nome: str) -> bool:
    """
    Verifica se o nome é válido.
    Deve conter apenas letras e espaços, com no mínimo 3 caracteres.
    """
    padrao = r"^[A-Za-zÀ-ÿ\s]{3,}$"
    return bool(re.match(padrao, nome.strip()))

def validar_codigo_disciplina(codigo: str) -> bool:
    """
    Verifica se o código da disciplina é válido.
    Deve ter entre 3 e 10 caracteres alfanuméricos.
    """
    padrao = r"^[A-Za-z0-9]{3,10}$"
    return bool(re.match(padrao, codigo.strip()))

def validar_opcao_menu(opcao: str, minimo: int, maximo: int) -> bool:
    """
    Verifica se a opção de menu é um número inteiro dentro do intervalo.
    """
    if not opcao.isdigit():
        return False
    return minimo <= int(opcao) <= maximo

def validar_carga_horaria(valor: str) -> bool:
    """
    Verifica se a carga horária é um número inteiro positivo.
    """
    return valor.isdigit() and int(valor) > 0

def validar_email(email: str) -> bool:
    """
    Verifica se o e-mail tem formato válido.
    (Funcionalidade extra para futura expansão do sistema.)
    """
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(padrao, email.strip()))

def validar_nao_vazio(valor: str) -> bool:
    """Verifica se o campo não está vazio."""
    return bool(valor.strip())
