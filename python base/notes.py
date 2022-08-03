""" Bloco de notas
$ notes.py new "Minha Nota"
tag: tecnologia
text:
Anotação geral sobre carreira de tecnologia

$ notes.py read tech
..
...
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")
cmds = ("read", "new")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print("Invalid command {arguments[0}")

if arguments[0] == "read":
    for line in open(filepath):
        titulo, tag, texto = line.split("\t")
        if tag == arguments[1].lower():
            print(f"Título: {titulo}")
            print(f"Texto: {texto}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    titulo = arguments[1] #TODO -> Tratar exception
    texto = [
        f"{titulo}",
        input("tag: ").strip(),
        input("text:\n").strip(),
    ]

    with open(filepath, "a") as file_:
        file_.write("\t".join(texto) + "\n")
