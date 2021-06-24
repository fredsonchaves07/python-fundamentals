"""
- Listas é um tipo de variável composta onde é possível armazenar mais de uma informação
- A lista pode conter vários elementos de diversos tipos de dados
- Uma boa prática é criar uma lista com mesmo tipo de dados
- As listas assim como as strings possui a técnica do fatiamento
"""

# Criação da lista vazia
list1 = []

# Criando uma lista com elementos
list2 = ['Python', 'C++', 'Java', 'Javascript']

# Adicionando elemento na lista
list2.append('Ruby')

# Adiciona elemento em uma determinada posição
list2.insert(0, 'Node')

# Remove o último elemento de uma lista
list2.pop()

# Remove todos os elementos da lista
list2.clear()

print(list2)