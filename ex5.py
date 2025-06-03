palavras = input("Digite palavras separadas por espaço: ").split()
# .split() = transforma a string digitada em uma lista de palavras

# lista vazia para guardar as palavras que serão filtradass
resultado = []

# Percorre cada palavra na lista 'palavras'
for p in palavras:
    if len(p) > 5:
        
        primeira_letra = p[0]
        
        # Verificação de  se a primeira letra é uma vogal (se está inclusa em "aeiouAEIOU") ou não
        if primeira_letra in 'aeiouAEIOU':
            # Caso realmente for, adiciona essa palavra na lista 'resultado'
            resultado.append(p)

# resultado
print("Palavras com mais de 5 letras e começando com vogal:")
print(resultado)
