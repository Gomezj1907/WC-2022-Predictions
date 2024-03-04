from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

driver = webdriver.Firefox()
"""web = 'https://en.wikipedia.org/wiki/1934_FIFA_World_Cup'

driver.get(web)

matches = driver.find_elements(by= 'xpath', value = '//div[@class="footballbox"]')

matches[6].text
"""
def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    driver.get(web)

    matches = driver.find_elements(by= 'xpath', value = '//tr[@style="font-size:90%"]')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find_element(by='xpath', value = './td[1]').text)
        score.append(match.find_element(by = 'xpath', value = './td[2]').text)
        away.append(match.find_element(by = 'xpath', value = './td[3]').text)

    dict_football = {'home':home, 'score': score, 'away':away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year

    print(df_football.shape, year)

    time.sleep(2)

    return df_football


years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
         2018]

fifa = [get_matches(year) for year in years]

driver.quit()

df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv("01_data_collect/output/fifa_worldcup_missing.csv", index=False)



driver.close()