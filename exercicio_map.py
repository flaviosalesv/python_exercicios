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



print(valor_emprestimos_lista)
