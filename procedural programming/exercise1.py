def duplicate_number(number_list: list):
    set_number = set()

    for number in number_list:
        if number in set_number:
            return number

        set_number.add(number)

    return -1


integer_numbers_list = [
    [1, 10, 2, 5, 6, 10, 2, 1, 3, 10],
    [2, 5, 3, 4, 2, 1, 9, 1, 9, 8, 6],
    [5, 7, 1, 1, 5, 9, 4, 3, 2, 1],
    [10, 6, 5, 7, 4, 6, 5, 9, 8, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
]

for number_list in integer_numbers_list:
    number = duplicate_number(number_list)
    print(number)
