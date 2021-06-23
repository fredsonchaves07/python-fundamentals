number = input('Digite um número inteiro: ')

if number.isnumeric():
    if int(number) % 2 == 0:
        print('Número digitado é par')
    else:
        print('Número digitado é impar')
else:
    print('Você não digitou um número inteiro')