import csv

emprestimos = []

with open(file='./credito.csv', mode='r', encoding='utf8') as fp:
    csv_reader = csv.reader(fp)
    
    next(csv_reader)
    
    linha = next(csv_reader, None)

    while linha:
        linha_emprestimo = {
            'id_vendedor': linha[0],
            'valor_emprestimos': linha[1],
            'quantidade_emprestimos': linha[2],
            'data': linha[3]
        }
        emprestimos.append(linha_emprestimo)
        
        linha = next(csv_reader, None)

for emprestimo in emprestimos:
    print(emprestimo)

