datetime = input('Digite a hora atual (hh:mm): ')

try:
    hours_datetime = datetime.split(':')[0]

    if int(hours_datetime) < 12:
        print('Bom dia')
    elif int(hours_datetime) < 17:
        print('Boa tarde')
    else:
        print('Boa noite')
except:
    print('Você não digitou conforme solicitado')