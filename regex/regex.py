import re

string = "Este é um teste de expressão teste regulares"
print(re.search(r"teste", string))
print(re.findall(r"teste", string))
print(re.sub(r"teste", r"ABCD", string))
