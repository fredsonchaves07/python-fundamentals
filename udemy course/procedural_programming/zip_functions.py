"""
- Funções utilizada para unir iteráveis
- A função zip retorna um interável e deixa a estrutura de dados mais dinâmica
- A união ocorre a partir da menor lista (Uni até terminar a lista)
- A função zip_longest uni de forma contrária a função zip
- Realiza a união a partir da maior lista (Lista menor fica com valor None)
"""
from itertools import zip_longest

city = ["São Paulo", "São Luís", "Salvador", "Icatu"]
uf = ["SP", "MA", "BA"]

city_uf = zip(uf, city)

# O parâmetro fillvalue troca o none pelo valor informado
city_uf2 = zip_longest(uf, city)

for value in city_uf:
    print(value)

for value in city_uf2:
    print(value)
