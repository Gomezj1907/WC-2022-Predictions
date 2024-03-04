import pandas as pd
import requests
from bs4 import BeautifulSoup

years = [
    1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 
    1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 
    2010, 2014, 2018
]

def get_matches(year):

    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    response = requests.get(web)

    content = response.text

    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_ = 'footballbox')


    home = []
    score = []
    away = []



    for match in matches:
        home.append(match.find('th', class_ ='fhome').get_text())
        score.append(match.find('th', class_ ='fscore').get_text())
        away.append(match.find('th', class_ ='faway').get_text())


    dict_football = {'home': home, 'score':score, 'away':away}

    df_football = pd.DataFrame(dict_football)
    df_football['year'] = f'{year}'
    print(df_football.shape, year)
    return df_football


fifa_wc = [get_matches(year) for year in years]

df_fifa_wc = pd.concat(fifa_wc, ignore_index=True)

# Partido repetido de Cuba- Romania tengo registor de penales y de partido hasta TE
df_fifa_wc[df_fifa_wc['year'] == '1938']

df_fifa_wc.to_csv('01_data_collect/output/historic_data.csv', index = False)





web = 'https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'

response = requests.get(web)

content = response.text

soup = BeautifulSoup(content, 'lxml')

matches = soup.find_all('div', class_ = 'footballbox')


home = []
score = []
away = []



for match in matches:
    home.append(match.find('th', class_ ='fhome').get_text())
    score.append(match.find('th', class_ ='fscore').get_text())
    away.append(match.find('th', class_ ='faway').get_text())


dict_football = {'home': home, 'score':score, 'away':away}

df_2022 = pd.DataFrame(dict_football)
df_2022['year'] = '2022'

df_2022.to_csv("01_data_collect/output/wc_2022.csv", index= False)


