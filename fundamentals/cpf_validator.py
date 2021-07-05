try:
    cpf = input('Digite o cpf: ')

    if len(cpf) < 11 or len(cpf) > 11:
        raise Exception

    cpf_checker_digits = cpf[-2:]
    sum_digit = 0
    result = 0

    for digit, cont in enumerate(range(10, 1, -1)):
        result = int(cpf[digit]) * cont
        sum_digit += result

    if(11 - (sum_digit % 11) > 9):
        first_digit = 0
    else:
        first_digit = 11 - (sum_digit % 11)

    if not first_digit == int(cpf_checker_digits[0]):
        raise Exception

    sum_digit = 0

    for digit, cont in enumerate(range(11, 2, -1)):
        result = int(cpf[digit]) * cont
        sum_digit += result
    
    result = first_digit * 2
    sum_digit += result

    second_digit = 11 - (sum_digit % 11)

    if not second_digit == int(cpf_checker_digits[1]):
        raise Exception
    
    print('CPF Válido')
except Exception:
    print('CPF inválido!')




