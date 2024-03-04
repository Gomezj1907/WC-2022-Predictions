import pandas as pd
from string import ascii_uppercase as alphabet
import pickle 
tablas_grupos = pd.read_html('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')

len(tablas_grupos)

# Cual es mi primera y ultima tabla (Van en patrones de 7)
tablas_grupos[9]
tablas_grupos[58]

for i in range(9,59, 7): 

    print(i)

# Print the alphabet
alphabet

# Link letters and numbers

dict_tables = {}
for letter, i in zip(alphabet, range(9,59, 7)) :
    df = tablas_grupos[i]
    df.rename(columns={ df.columns[1]: 'Team'}, inplace=True)
    df.pop('Qualification')
    dict_tables[f'Group {letter}'] = df

dict_tables.keys()

dict_tables['Group A']

with open('01_data_collect/output/dict_tables', 'wb') as output:
    pickle.dump(dict_tables, output)