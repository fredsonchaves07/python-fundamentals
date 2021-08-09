"""
- Ideal para manipulação de arquivos e banco de dados
- Realiza o fechamento automaticamente
- Podemos criar nossos próprios gerenciador de contexto
"""


# Estrutura básica da classe para aceitar gerenciador de contexto
class File:
    def __init__(self, file, operation):
        self.file = open(file, operation)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with File("abc.txt", "w") as file:
    file.write("Python ..")
