def Situação_aluno_calculadora():
    nota1 = float(input("Nota gq1: "))
    nota2 = float(input("Nota gq2: "))

    interface = ("\n-" * 35) * 2

    nota_final = (nota1 * 2 + nota2 * 3) / 5

    if nota_final >= 10:
        return print(interface + print("---------GABRITOU!!!-----------") + interface)
    elif nota_final < 10 and nota_final >= 7:
        return print(interface + print("-------PASSOU POR MÉDIA!--------") + interface)
    elif nota_final < 7 and nota_final >= 4:
        return print(interface + print("-----FOI PARA RECUPERAÇÃO-------") + interface)
    elif nota_final < 4:
        return print(interface + print("---------NÃO PASSOU...----------") + interface)
    else:
         print("\n\n\n\n\n\n\n\n|||ERROR|||")
         return breakpoint()


Situação_aluno_calculadora()
    
