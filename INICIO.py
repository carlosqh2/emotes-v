import quandl as qd
import pandas as pd
import math
from sklearn.model_selection import cross_validate, train_test_split
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression

df = qd.get('WIKI/GOOGL')
# print(df.head())
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]

# Diferencia del cambio
df['HL_PCT']= 100.0*(df['Adj. High']-df['Adj. Close'])/df['Adj. Close']
#Cambio Porcentaje Diario
df['PCT_Cambio']= 100.0*(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']

df = df[['Adj. Close', 'HL_PCT', 'PCT_Cambio', 'Adj. Volume']]

#Columna del pronóstico
col_pronostico = 'Adj. Close'
df.fillna(-99999, inplace = True)

pronostico_out = int(math.ceil(0.01*len(df)))
df['etiqueta'] = df[col_pronostico].shift(-pronostico_out)

print(df.tail())
df.dropna(inplace = True)
