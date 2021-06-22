from datetime import datetime

name = input('Digite o nome: ')
age = int(input('Digite a idade: '))
height = float(input('Digite a altura: '))
weight = float(input('Digire o peso: '))
current_year = datetime.now().year

imc = weight / (height ** 2)

print(f'Seu IMC é igual a {imc:.2f}')
print(f'Seu ano de nascimento é {current_year - age}')
