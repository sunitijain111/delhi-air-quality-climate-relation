import pandas as pd
import numpy as np
df1= pd.read_excel('delhi air 1996 to 2015.xls')
df2= pd.read_excel('delhi weather since 1997.xlsx') 

df3= pd.merge(df1, df2, how='inner', on=['month','year'])
df3.fillna(df3.mean(), inplace= True)

df3=df3.drop('PM 2.5', axis=1)
