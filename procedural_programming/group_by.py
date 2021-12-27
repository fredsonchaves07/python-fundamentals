"""
Realiza o agrupamento por um determinado campo
Necessário que o dado seja ordenado para que seja realizado o agrupamento
"""
from itertools import groupby

students = [
    {"name": "Fredson", "avg": 10},
    {"name": "Ana", "avg": 10},
    {"name": "Luiza", "avg": 6},
    {"name": "Carol", "avg": 8},
    {"name": "Carlos", "avg": 10},
    {"name": "Roberto", "avg": 2},
    {"name": "Mario", "avg": 0},
    {"name": "Joana", "avg": 5},
]
students.sort(key=lambda student: student["avg"])
students_group = groupby(students, lambda student: student["avg"])

for group, students in students_group:
    print(group)
    for student in students:
        print(student)
    print()
