def validar_nome(nome):
    nome = nome.strip()

    if nome == "":
        raise ValueError("O nome não pode ficar vazio.")

    if len(nome) < 3:
        raise ValueError("O nome deve ter pelo menos 3 letras.")

    return nome.title()


def validar_matricula(matricula):
    matricula = matricula.strip()

    if matricula == "":
        raise ValueError("A matrícula não pode ficar vazia.")

    if not matricula.isdigit():
        raise ValueError("A matrícula deve ter apenas números.")

    return matricula


def validar_nota(nota):
    try:
        nota = float(nota)
    except:
        raise ValueError("A nota precisa ser um número.")

    if nota < 0 or nota > 10:
        raise ValueError("A nota deve estar entre 0 e 10.")

    return nota
