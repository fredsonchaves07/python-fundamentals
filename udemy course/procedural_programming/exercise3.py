carrinho = []

carrinho.append(("Produto 1", 30))
carrinho.append(("Produto 2", 20))
carrinho.append(("Produto 3", 50))

total = [float(preco) for nome, preco in carrinho]

print(sum(total))
