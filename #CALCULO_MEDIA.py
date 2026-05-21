#CALCULO_MEDIA


nota_aluno1 = float(input("Digite a nota do seu primeiro Gq:  "))
nota_aluno2 = float(input("Digite a nota do seu segundo Gq:  "))

calcular_media = ((nota_aluno1 * 2) + (nota_aluno2 * 3)) / 5

if calcular_media >= 7:
    print(f"Parabéns, sua nota foi {calcular_media:.2f} e você passou por média!!")

else:
    print(f"Sua nota foi {calcular_media:.2f}.")