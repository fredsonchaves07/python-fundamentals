"""
Combinations, Permutations e Product - Funções do itertools
combinations -> Combinações de elementos onde a ordem não importa
permutations -> Combinações de elementos onde a ordem importa
product -> Todas as combinações possíveis
"""
from itertools import combinations, permutations, product

peoples = ["Fredson", "Darlynne", "Anna"]

for group in combinations(peoples, 3):
    print(group)


for group in permutations(peoples, 3):
    print(group)

for group in product(peoples, repeat=2):
    print(group)
