print("Digite a primeira lista de palavras (separadas por espaço):")
lista1 = input().split()

print("\nDigite a segunda lista de palavras (separadas por espaço):")
lista2 = input().split()

# Converte/seta as listas em conjuntos e calcula a interseção
interseção = set(lista1) & set(lista2)


print("\n Palavras que aparecem nas duas listas:")
if interseção:                            #se o conjunto não está vazio,
    for palavra in sorted(interseção):    #percorre as palavras em comum / em interseção
        print(f"{palavra}")
else:
    print("Nenhuma palavra em comum")
    