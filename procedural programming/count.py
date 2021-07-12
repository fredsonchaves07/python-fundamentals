"""
- Realiza a contagem dos iteradores
- Iterador que não tem fim, a cada vez que pedir o valor, será retornado o valor
- Loop infinito
"""
from itertools import count

cont = count()

print(next(cont))

# Podemos iniciar o contador e definir os passos
cont = count(start=5, step=1)
