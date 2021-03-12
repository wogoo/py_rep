import requests
import time 
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = "https://www.ogol.com.br/player_seasons.php?id=548752"
option = Options()
option.headless = True 
driver = webdriver.Firefox()

driver.get(url)
time.sleep(10)

driver.find_element_by_xpath("//div[@id='team_games']//table//thead//tr//th[@class='double']").click()
element = driver.find_element_by_xpath("//div[@id='team_games']//table")
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full = pd.read_html(str(table)) [0].head(5)
df = df_full[['Temporada', 'Clube', 'J', 'GM']]
df.columns = ['Temporada','clube', 'jogos', ' ' 'Gols']


teamsPlayer = {}
teamsPlayer['teams'] = df.to_dict('records')


driver.quit()

js = json.dumps(teamsPlayer)
fp = open('clubess.json', 'w')
fp.write(js)
fp.close()