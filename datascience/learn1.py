from pandas import DataFrame, Series

atti_datal = {'ID': [1, 2, 3, 4],
              'City': ['Tokyo', 'Fukuoka', 'kitakyu', 'unknow'],
              'sex': ['M', 'F', 'F', 'M'],
              }

df_atti_datal = DataFrame(atti_datal)

print(df_atti_datal.T)