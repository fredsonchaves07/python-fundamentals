"""
- Realiza a enumeração de uma lista
"""

lista = ['Python', 'Java', 'Javascript']

for v1, v2 in enumerate(lista):
    print(v1, v2)

# É possível manipular a enumeração, escolhendo qual número a iniciar
for v1, v2 in enumerate(lista, 10):
    print(v1, v2)