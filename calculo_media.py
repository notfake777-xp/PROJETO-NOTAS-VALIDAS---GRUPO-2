#CALCULO_MEDIA

def calcular_media():
    print("\n=== CÁLCULO DE MÉDIA ===")

    nota1 = float(input("Digite a nota do seu primeiro GQ: "))
    nota2 = float(input("Digite a nota do seu segundo GQ: "))

    media = ((nota1 * 2) + (nota2 * 3)) / 5

    if media >= 7:
        print(f"\nParabéns! Sua média foi {media:.2f} e você passou!\n")
    else:
        print(f"\nSua média foi {media:.2f}. Você não atingiu a média.\n")

    return media