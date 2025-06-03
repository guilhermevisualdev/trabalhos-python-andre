frase = input("Digite uma frase: ")

# Substitui cada vogal por *
frase_modificada = ""
for letra in frase:                           #para cada letra (vogal) na frase, será substituída por "*"
    if letra in 'aeiouAEIOU' :
        frase_modificada += "*"
    else:
        frase_modificada += letra


print("\nFrase mascarada:")
print(frase_modificada)

