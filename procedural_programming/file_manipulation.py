# Python trata arquivos com biblioteca padrão de manipulação de arquivos
# Forma pythônica de gerenciamento de arquivos -> Gerenciamento de contexto
# Evita erros de não fechamento do arquivo
with open("abc.txt", "w+") as file:
    file.write("Linha 1")

    print(file.read())
