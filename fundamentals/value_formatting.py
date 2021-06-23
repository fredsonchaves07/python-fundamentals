"""
- Os valores podem ser formatados utilizando a função format ou até mesmo com f strings
- As formatações obedecem as regras
- :s -> Texto(strings)
- :d -> Inteiros(int)
- :f -> Números de pinto flutuante
"""
number1 = 10
number2 = 3
divison = number1 / number2

# Formatando em casas decimais com format
print('{:.2f}'.format(divison))
# Formatando em casas decimais com fstring
print(f'{divison:.2f}')
# Podemos formatar contando digitos / caracter e preencher com zeros ou caracter
# > (Esquerda); < (Direita); ^ (Centro)
number3 = 1
print(f'{number3:0<10d}')