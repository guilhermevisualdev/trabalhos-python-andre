def aluno_maior_nota(lista_alunos):
    aluno_maior = ("", -1)                                
    for nome, nota in lista_alunos:                       # percorre cada tupla através do for (nomes e notas)
        if nota > aluno_maior[1]:                         # se a nota atual for maior que a guardada,
            aluno_maior = (nome, nota)                    # atualiza a tupla com o novo aluno
    return aluno_maior[0]                                 

# Entrada do usuário
alunos = []                                               # armazenar os alunos dentro
qtd = int(input("Quantos alunos deseja inserir? "))       

for i in range(qtd):
    nome = input(f"Nome do aluno {i+1}: ")                
    while True:
        try:
            nota = float(input(f"Nota de {nome}: "))      # tenta converter a nota para número
            break                                         # se der certo, sai do loop ("quebra" o looping e prosseguee para a próxima linha)
        except ValueError:                                # verificação se possui algo errado / foi digitado errado
            print("Nota inválida. Digite um número.")
    alunos.append((nome, nota))                           # tupla de nome e nota



# resultados
if alunos:                                                
    melhor = aluno_maior_nota(alunos)                    
    print(f"\nO Aluno com a maior nota é: {melhor}")   
