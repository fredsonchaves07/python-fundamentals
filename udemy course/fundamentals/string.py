"""
    fstrings -> Exibi valores formatados
    format -> Outra forma de exibir valores formatados
"""
name = 'Fredson Chaves'
age = 26

print(f'{name} tem {age} anos')
print('{} tem {} anos'.format(name, age) )
# Parâmetros nomeados na função format. É possível alterar a ordem
print('{n} tem {a} anos'.format(n=name, a=age))
