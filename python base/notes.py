""" Bloco de notas
$ notes.py new "Minha Nota"
tag: tecnologia
text:
Anotação geral sobre carreira de tecnologia

$ notes.py read --tag=tech
..
...
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    sys.exit(1)

cmds = ("read", "new")
if arguments[0] not in cmds:
    print("Invalid command {arguments[0}")

if arguments[0] == "read":
    # Leitura das notas
    pass

if arguments[0] == "new":
    titulo = arguments[1] #TODO -> Tratar exception
    texto = [
        f"{titulo}\n",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]