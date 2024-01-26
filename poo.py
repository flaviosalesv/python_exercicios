class ArquivoTexto:
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self.ler_arquivo()

    def ler_arquivo(self):
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Arquivo '{self.arquivo}' não encontrado.")
            return []

    def extrair_linha(self, numero_linha: int):
        if 1 <= numero_linha <= len(self.conteudo):
            return self.conteudo[numero_linha - 1].strip()
        else:
            return f"Linha {numero_linha} fora do intervalo válido."


arquivo_texto = ArquivoTexto(arquivo='musica.txt')

numero_linha = 1
print(arquivo_texto.extrair_linha(numero_linha=numero_linha))

numero_linha = 10
print(arquivo_texto.extrair_linha(numero_linha=numero_linha))

#############

class ArquivoCSV(ArquivoTexto):
    def __init__(self, arquivo: str):
        super().__init__(arquivo)
        if self.conteudo:
            self.colunas = self.conteudo[0].strip().split(',')
        else:
            self.colunas = []

    def extrair_coluna_da_linha(self, numero_linha: int, numero_coluna: int):
        if 1 <= numero_linha <= len(self.conteudo):
            linha = self.conteudo[numero_linha - 1].strip().split(',')
            if 0 <= numero_coluna < len(linha):
                return linha[numero_coluna].strip()
            else:
                return f"Coluna {numero_coluna} fora do intervalo válido."
        else:
            return f"Linha {numero_linha} fora do intervalo válido."


arquivo_csv = ArquivoCSV(arquivo='carros.csv')

numero_linha = 1
print(arquivo_csv.extrair_linha(numero_linha=numero_linha)) 
print(arquivo_csv.colunas) 

numero_linha = 10
print(arquivo_csv.extrair_linha(numero_linha=numero_linha))

numero_coluna = 2
print(
    arquivo_csv.extrair_coluna_da_linha(
        numero_linha=numero_linha,
        numero_coluna=numero_coluna
    )
)  
