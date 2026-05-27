# ============================================================
# BRANCH: Develop
# RESPONSÁVEL: Danilo
# DESCRIÇÃO: Ambiente de testes e integração do sistema
#            Use esta branch para testar antes de enviar
#            para a branch Main via Pull Request.
# ============================================================

from cadastro_aluno import cadastrar_aluno, listar_alunos, buscar_aluno
from cadastro_disciplina import cadastrar_disciplina, listar_disciplinas, buscar_disciplina
from inserir_notas import inserir_nota
from calculo_media import calcular_media, obter_media_aluno
from situacao_aluno import verificar_situacao
from historico_aluno import exibir_historico
from validacoes import (
    validar_nota, validar_matricula, validar_nome,
    validar_codigo_disciplina, validar_opcao_menu
)

# ============================================================
# TESTES AUTOMATIZADOS SIMPLES
# ============================================================

def testar_validacoes():
    """Testa as funções do módulo validacoes.py"""
    print("\n[TESTE] Validações:")

    assert validar_nota("8.5") == True, "Nota 8.5 deveria ser válida"
    assert validar_nota("10") == True, "Nota 10 deveria ser válida"
    assert validar_nota("10.1") == False, "Nota 10.1 deveria ser inválida"
    assert validar_nota("abc") == False, "Texto não é nota válida"
    assert validar_nota("-1") == False, "Nota negativa inválida"

    assert validar_matricula("12345") == True, "Matrícula numérica válida"
    assert validar_matricula("123") == False, "Matrícula curta inválida"
    assert validar_matricula("abc") == False, "Matrícula com letras inválida"

    assert validar_nome("João Silva") == True, "Nome válido"
    assert validar_nome("AB") == False, "Nome muito curto"
    assert validar_nome("Jo@o") == False, "Nome com caractere especial"

    assert validar_codigo_disciplina("MAT01") == True, "Código válido"
    assert validar_codigo_disciplina("AB") == False, "Código curto demais"

    assert validar_opcao_menu("3", 1, 8) == True, "Opção 3 válida"
    assert validar_opcao_menu("9", 1, 8) == False, "Opção 9 fora do range"
    assert validar_opcao_menu("x", 1, 8) == False, "Opção texto inválida"

    print("  ✅ Todas as validações passaram!\n")


def testar_integracao():
    """
    Testa fluxo de integração: busca aluno + médias.
    Requer dados já cadastrados no sistema.
    """
    print("[TESTE] Integração (busca aluno + médias):")
    matricula = input("  Digite uma matrícula para testar: ").strip()

    aluno = buscar_aluno(matricula)
    if aluno:
        print(f"  ✅ Aluno encontrado: {aluno['nome']}")
        medias = obter_media_aluno(matricula)
        if medias:
            for cod, info in medias.items():
                print(f"     Disciplina {cod}: Média {info['media']} - {info['status']}")
        else:
            print("  [!] Nenhuma nota registrada para teste de médias.")
    else:
        print("  [!] Aluno não encontrado. Cadastre primeiro pelo main.py.")


def menu_develop():
    """Menu de opções para ambiente de desenvolvimento."""
    print("=" * 50)
    print("     AMBIENTE DE TESTES - DEVELOP")
    print("=" * 50)
    print("\n  [1] Rodar testes de validação")
    print("  [2] Testar integração (busca + médias)")
    print("  [3] Sair")

    opcao = input("\n  Opção: ").strip()

    if opcao == "1":
        testar_validacoes()
    elif opcao == "2":
        testar_integracao()
    elif opcao == "3":
        print("\n  Saindo do ambiente de testes.\n")
    else:
        print("\n  [!] Opção inválida.")


if _name_ == "_main_":
    menu_develop()