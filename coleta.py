import pandas as pd
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time


def coleta_camisa(url):
    print("OK1")
    page = requests.get(url)
    print(page)

    soup = BeautifulSoup(page.content, 'html.parser')
    nome = soup.find('h2').text.replace("/", "-")


    all_imagem_page = soup.find_all(class_="showalbum__children image__main")
    u = all_imagem_page[0].find("img").attrs["data-origin-src"]

    print(u)

    # criar pasta com o nome da camisa
    nome_pasta = ""
    for i in range(1000):
        if not os.path.exists(f"imagem_camisa/{nome}_{i}"):
            nome_pasta = f"imagem_camisa/{nome}_{i}"
            os.makedirs(nome_pasta)
            break


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--unlimited-storage")
    prefs = {
        "download.default_directory" : f"/Users/jair/Documents/github/scrapyCamisas/scrapyDados/{nome_pasta}",
        'profile.default_content_setting_values.automatic_downloads': 1
    }
    chrome_options.add_experimental_option("prefs",prefs)
    
    # 
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    
    print("Iniciando selenium")
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=chrome_options)


    driver.get(url)
    time.sleep(5)


    driver.execute_script(f'var a = document.createElement("a"); a.href = "https:{u}"; a.download = "teste.jpeg"; a.click();')
    time.sleep(2)

    for i in range(len(all_imagem_page)):
        driver.execute_script(f'var a = document.createElement("a"); a.href = "https:{all_imagem_page[i].find("img").attrs["data-origin-src"]}"; a.download = "{nome}_{i}.jpeg"; a.click();')
        time.sleep(2)
    

    driver.quit()
    # driver.close()


# print(nome)