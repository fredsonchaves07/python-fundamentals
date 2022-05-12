"""
- Podemos utilizar a função `len` para realizar a contagem de strings
e outros tipos de dados como dicionários, listas etc.
- Ao chamar a função `len` dentro de uma string, por baixo dos panos, 
o python executa `string.__len__()`
- A função `len` não realiza a contagem em tipos inteiros, float e booleanos
"""

user = input('Digite seu usuário: ')
count = len(user)

print(user, count)

if count < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Cadastrado com sucesso!')