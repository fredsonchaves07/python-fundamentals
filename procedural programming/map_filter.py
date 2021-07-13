"""
Alguma das funções úteis que podemos utilizar
map, filter
"""

products = [
    {"name": "Computador", "price": 3299.00},
    {"name": "Monitor", "price": 1250.99},
    {"name": "Mouse", "price": 80.00},
    {"name": "Teclado Mecânico", "price": 80.00},
    {"name": "Impressora", "price": 1569.80},
]

customer = [
    {"name": "Fredson", "age": 26},
    {"name": "Carlos", "age": 15},
    {"name": "Ana", "age": 30},
    {"name": "Maria", "age": 26},
]

list1 = [1, 2, 3, 5, 6, 7, 9, 10]

# Cria uma nova lista mapeada de acordo com as regras das funções lambdas
# Uma alternativa seria utilizar as list comprehensions
list2 = map(lambda x: x * 2, list1)

print(list(list2))

# O Map pode ser interessante em dados do tipo dicionário
# Retorna a lista com os produtos com o desconto
discount = 0.15
product_discount = map(
    lambda product: product.get("price") - (product["price"] * discount), products
)

print(list(product_discount))
