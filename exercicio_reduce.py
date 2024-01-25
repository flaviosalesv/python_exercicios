import csv
import math
from functools import reduce

emprestimos = []

with open(file='./credito.csv', mode='r', encoding='utf8') as fp:
    csv_reader = csv.reader(fp)
    
    next(csv_reader)
    
    emprestimos = list(map(lambda linha: {
        'id_vendedor': linha[0],
        'valor_emprestimos': linha[1],
        'quantidade_emprestimos': linha[2],
        'data': linha[3]
    }, csv_reader))

valor_emprestimos_lista = list(map(lambda x: float(x['valor_emprestimos']), emprestimos))

valor_emprestimos_lista_filtrada = list(filter(lambda x: x > 0, valor_emprestimos_lista))

soma_valor_emprestimos = reduce(lambda x, y: x + y, valor_emprestimos_lista_filtrada, 0)

print(soma_valor_emprestimos)


#Média
media_valor_emprestimos = reduce(lambda x, y: x + y, valor_emprestimos_lista_filtrada, 0) / len(valor_emprestimos_lista_filtrada)

print(media_valor_emprestimos)

#Desafio
media = reduce(lambda x, y: x + y, valor_emprestimos_lista_filtrada, 0) / len(valor_emprestimos_lista_filtrada)

soma_quadrados_diff = reduce(lambda x, y: x + (y - media) ** 2, valor_emprestimos_lista_filtrada, 0)
variancia = soma_quadrados_diff / (len(valor_emprestimos_lista_filtrada) - 1)  # Correção aqui
desvio_padrao_valor_emprestimos = math.sqrt(variancia)

print(desvio_padrao_valor_emprestimos)