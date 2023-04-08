"""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import lxml
import time
options = Options()
driver = webdriver.Chrome(options=options)
driver.get ("https://store.steampowered.com/?l=russian")
search = driver.find_element(by="id", value="store_nav_search_term")
search.send_keys("стратегии")
search.send_keys(Keys.ENTER)
time.sleep(3)
page=driver.page_source
soup=BeautifulSoup(page, "lxml")
conteiner = soup.find("div", "search_results")
names=conteiner.find_all("span", "title")
for i in names:
    print(i.text)