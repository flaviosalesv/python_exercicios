import csv


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

print(valor_emprestimos_lista_filtrada)
