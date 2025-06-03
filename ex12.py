produtos = {
    'GTR R35': 1500000,
    'Mondeo': 21000,
    'Mazda 626': 10000,
    'Del Rey': 5000,
    'Chevette': 7500
}

# lista os itens em ordem do menor (valor) para o maior (valor)
ordenados = sorted(produtos.items(), key=lambda item: item[1])        # "key=lambda item: item[1]"  ->  fala para ordenar pelo preço


print("Produtos do mais barato ao mais caro:")
for produto, preco in ordenados:
    print(f"- {produto}: R${preco:.2f}")