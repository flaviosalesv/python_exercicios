import csv

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):
    coluna = []

    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        
        
        next(leitor)

        for linha in leitor:
            if indice_coluna < len(linha):
                valor = linha[indice_coluna].strip()
                
                
                if valor != '':
                    
                    if tipo_dado == 'int':
                        valor = int(valor)
                    elif tipo_dado == 'float':
                        valor = float(valor)
                    elif tipo_dado == 'str':
                        valor = str(valor)

                    coluna.append(valor)

    return coluna


pessoas = extrai_coluna_csv(
    nome_arquivo='./carros.csv',
    indice_coluna=4,
    tipo_dado='int'
)
print(pessoas)
