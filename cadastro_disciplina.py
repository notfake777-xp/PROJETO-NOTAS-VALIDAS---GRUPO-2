banco_disciplinas = [
    {"codigo": "FP01", "nome": "Fundamentos da programação", "carga_horaria": 80},
    {"codigo": "FH01", "nome": "Fundamentos de hardware", "carga_horaria": 60},
    {"codigo": "EDC01", "nome": "Elementos da diferenciação computacional", "carga_horaria": 80},
    {"codigo": "LMAC01", "nome": "Lógica Matematica Aplicada a Computação", "carga_horaria": 70},
    {"codigo": "ICC01", "nome": "Introdução a ciencia da computação", "carga_horaria": 80},
    {"codigo": "HT01", "nome": "Humanidade e transcedencia", "carga_horaria": 60}
]

def encontrar_disciplina(codigo):
    """Função auxiliar para encontrar uma disciplina pelo código."""
    for disc in banco_disciplinas:
        if disc['codigo'] == codigo:
            return disc
    return None

def inserir_disciplina():
    print("\n--- CADASTRO DE DISCIPLINA ---")
    codigo = input("Digite o código da disciplina (ex: COMP01): ").strip().upper()

    if encontrar_disciplina(codigo):
        print(f"❌ Erro: Uma disciplina com o código '{codigo}' já existe.")
        return

    nome = input("Digite o nome da disciplina: ").strip()

    while True:
        try:
            carga_horaria = int(input("Digite a carga horária (apenas números): "))
            if carga_horaria <= 0:
                print("Erro: A carga horária deve ser um número positivo.")
            else:
                break
        except ValueError:
            print("Erro: A carga horária precisa ser um número inteiro!")

    if not nome or carga_horaria <= 0:
        print("Erro: Dados inválidos. Preencha o nome e a carga horária corretamente.")
        return

    nova_disciplina = {
        "codigo": codigo,
        "nome": nome,
        "carga_horaria": carga_horaria
    }

    banco_disciplinas.append(nova_disciplina)
    print(f"✅ Disciplina '{nome}' (Código: {codigo}) inserida com sucesso!")

def listar_disciplinas():
    print("\n--- LISTA DE DISCIPLINAS CADASTRADAS ---")
    if not banco_disciplinas:
        print("Nenhuma disciplina cadastrada até o momento.")
        return

    for idx, disc in enumerate(banco_disciplinas, start=1):
        print(f"{idx}. [{disc['codigo']}] {disc['nome']} - Carga Horária: {disc['carga_horaria']}h")

def buscar_disciplina():
    print("\n--- BUSCAR DISCIPLINA ---")
    codigo = input("Digite o código da disciplina para buscar: ").strip().upper()
    disciplina = encontrar_disciplina(codigo)

    if disciplina:
        print(f"\nDisciplina Encontrada:")
        print(f"  Código: {disciplina['codigo']}")
        print(f"  Nome: {disciplina['nome']}")
        print(f"  Carga Horária: {disciplina['carga_horaria']}h")
    else:
        print(f"❌ Erro: Disciplina com código '{codigo}' não encontrada.")

def atualizar_disciplina():
    print("\n--- ATUALIZAR DISCIPLINA ---")
    codigo = input("Digite o código da disciplina para atualizar: ").strip().upper()
    disciplina = encontrar_disciplina(codigo)

    if disciplina:
        print(f"Atualizando disciplina: {disciplina['nome']} (Código: {disciplina['codigo']})")
        novo_nome = input(f"Novo nome da disciplina (atual: {disciplina['nome']}, deixe em branco para manter): ").strip()

        while True:
            nova_carga_horaria_str = input(f"Nova carga horária (atual: {disciplina['carga_horaria']}h, deixe em branco para manter): ").strip()
            if not nova_carga_horaria_str:
                nova_carga_horaria = disciplina['carga_horaria']
                break
            try:
                nova_carga_horaria = int(nova_carga_horaria_str)
                if nova_carga_horaria <= 0:
                    print("Erro: A carga horária deve ser um número positivo.")
                else:
                    break
            except ValueError:
                print("Erro: A carga horária precisa ser um número inteiro!")

        if novo_nome:
            disciplina['nome'] = novo_nome
        disciplina['carga_horaria'] = nova_carga_horaria
        print(f"✅ Disciplina '{disciplina['codigo']}' atualizada com sucesso!")
    else:
        print(f"❌ Erro: Disciplina com código '{codigo}' não encontrada.")

def remover_disciplina():
    print("\n--- REMOVER DISCIPLINA ---")
    codigo = input("Digite o código da disciplina para remover: ").strip().upper()
    disciplina = encontrar_disciplina(codigo)

    if disciplina:
        confirmacao = input(f"Tem certeza que deseja remover '{disciplina['nome']}' (Código: {disciplina['codigo']})? (s/n): ").strip().lower()
        if confirmacao == 's':
            banco_disciplinas.remove(disciplina)
            print(f"✅ Disciplina '{disciplina['nome']}' (Código: {disciplina['codigo']}) removida com sucesso!")
        else:
            print("Operação de remoção cancelada.")
    else:
        print(f"❌ Erro: Disciplina com código '{codigo}' não encontrada.")

def menu_principal():
    while True:
        print("\n==========================")
        print("  SISTEMA DE DISCIPLINAS   ")
        print("==========================")
        print("1. Inserir Disciplina")
        print("2. Listar Disciplinas")
        print("3. Buscar Disciplina")
        print("4. Atualizar Disciplina")
        print("5. Remover Disciplina")
        print("6. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            inserir_disciplina()
        elif opcao == "2":
            listar_disciplinas()
        elif opcao == "3":
            buscar_disciplina()
        elif opcao == "4":
            atualizar_disciplina()
        elif opcao == "5":
            remover_disciplina()
        elif opcao == "6":
            print("Saindo do sistema.")
            break
        else:
            print("❌ Opção inválida! Por favor, escolha um número entre 1 e 6.")

if __name__ == "__main__":
    menu_principal()
