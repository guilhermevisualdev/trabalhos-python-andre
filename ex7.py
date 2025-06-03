import string  # Importa a biblioteca que tem símbolos de pontuação

frase = input("Digite uma frase: ") 

for pontuacao in string.punctuation:  # Passa por todos e cada símbolo de pontuação que existem
    frase = frase.replace(pontuacao, '')  # Substitui esse símbolo na frase por nada (vazio)(remove)

palavras = frase.split()  # Separa a frase em palavras, criando uma lista de palavras

frequencia = {}  # Cria um dicionário vazio ("{}") para guardar as palavras e quantas vezes elas aparecem

for palavra in palavras:  # Para cada item na lista chamada palavras o Python vai pegar uma palavra por vez dessa lista e colocar ela na variável chamada palavra, Aí o código dentro desse for vai ser executado usando essa palavra atual.
    if palavra in frequencia:  # Se a palavra já está no dicionário
        frequencia[palavra] += 1  
    else:  # Se a palavra ainda não está no dicionário
        frequencia[palavra] = 1 

for palavra, qtd in frequencia.items(): 
    print(f"{palavra}: {qtd}")  # Mostra a palavra e quantas vezes apareceu
