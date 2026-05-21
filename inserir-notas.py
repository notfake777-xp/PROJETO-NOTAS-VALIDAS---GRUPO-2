# variável que armazena as notas
def notas():
    while True:

        nota1 = int(input("Insira sua primeira nota: "))
        nota2 = int(input("Insira sua sua segunda nota: "))
    
        print(f"Sua primeira nota é: {nota1} \nSua segunda nota é: {nota2}")
    
notas()