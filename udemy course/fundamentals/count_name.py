name = input('Digite o seu nome: ')

count_char_name = len(name)

if count_char_name < 4:
    print('Seu nome é curto')
elif count_char_name <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')