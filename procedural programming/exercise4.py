list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 2, 3, 4]

list_sum = [sum(value) for value in zip(list1, list2)]

print(list_sum)
