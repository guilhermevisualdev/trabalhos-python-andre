def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma


lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 40, 100, 103]
resultado = soma_pares(lista_teste)
print("Soma dos pares:", resultado)
