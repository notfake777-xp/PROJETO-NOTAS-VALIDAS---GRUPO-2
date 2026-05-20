historico_aluno() ###precisa da continuação disso

def definir_status(nota,nome_do_aluno):
    nome_do_aluno == input("Nome do aluno: ")


    find(nome_do_aluno in Historico_aluno) ##encontrar o aluno no histórico
    #encontrar a nota
    find(nota in nome_do_aluno) ###(vou ajeitar isso futuramente)
    
    
    
    
    
    
    ##lógica das notas:
    
    if nota >= 7:
        return print("ALUNO APROVADO")
    elif nota <= 7 and nota >= 5:
        return print("EM RECUPERAÇÃO")
    else:
        return print("REPROVADO")

