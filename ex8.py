# Abre o arquivo para realizar a *leitura*
with open("frases.txt", "r") as arquivo_entrada:
    palavras = set()
    
    for linha in arquivo_entrada:                           # Lê linha por linha do arquivo através do loop "for"
        
        for palavra in linha.strip().split():               # "transforma" linha em palavras (considera espaços)
            palavras.add(palavra)                           # adiciona as palavras
    
# Ordena as palavras únicas em ordem alfabética (sorted)
palavras_ordenadas = sorted(palavras)


with open("palavras_unicas.txt", "w") as arquivo_saida:         # Abre um arquivo para agora *escrever* as palavras
    for palavra in palavras_ordenadas:                          # para palavra em palavras_ordenadas,
        arquivo_saida.write(palavra + "\n")                     # escreve no arquivo a palavra e pula uma linha com o \n

print("Processo feito! As palavras únicas foram salvas em 'palavras_unicas.txt'.")
print("Programa bem-sucedido, finalizando...")
