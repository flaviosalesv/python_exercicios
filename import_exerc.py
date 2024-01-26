import wget
import zipfile
import os
import pandas as pd
import seaborn as sns

wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/' + '00312/dow_jones_index.zip', out='./dados.zip' )
with zipfile.ZipFile('./dados.zip', 'r') as fp:   fp.extractall('./dados')
os.rename('./dados/dow_jones_index.data', './dados/dow_jones_index.csv')
df = pd.read_csv('./dados/dow_jones_index.csv')

df.head(n=10)
print(df.head(n=10))

df.columns.to_list()
print(df.columns.to_list())

linhas, colunas = df.shape 
print(f'Número de linhas: {linhas}') 
print(f'Número de colunas: {colunas}') 

df_ko = df[df['stock'] == 'KO'] 
print(df_ko)

df_ko = df_ko[['date', 'open', 'high', 'low', 'close']]
print(df_ko)


for col in ['open', 'high', 'low', 'close']:   df_ko[col] = df_ko[col].apply(lambda value: float(value.split(sep='$')[-1])   )

df_ko.head(n=10)
df_ko.dtypes


#######

plot = sns.lineplot(
    x="date", 
    y="value", 
    hue='variable', 
    data=pd.melt(df_ko,['date'])
)
_= plot.set_xticklabels(labels=df_ko['date'], rotation=90) 


plot.figure.savefig("./ko.png")