def extrai_linha_txt(nome_arquivo: str, numero_linha: int):
    palavras_linha = []

    with open(nome_arquivo, 'r') as arquivo_txt:
        
        linhas = arquivo_txt.readlines()

        
        if 0 <= numero_linha < len(linhas):
            
            linha = linhas[numero_linha]

            
            palavras_linha = linha.split()

    return palavras_linha


nome_arquivo = 'musica.txt'
numero_linha = 4  
palavras = extrai_linha_txt(nome_arquivo, numero_linha)
print(palavras)
