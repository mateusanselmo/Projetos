from selenium import webdriver
from time import sleep
from credenciais import *

##### MENSAGEM #####
msg = "--*--"

# Browser
url = "https://twitter.com/"
ChromeConfig = webdriver.ChromeOptions()
ChromeConfig.add_argument("--incognito")
nav = webdriver.Chrome()
nav.get(url)

# PÁGINA INICIAL
sleep(2)
botao_0 = nav.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/a[2]/div/span/span")
botao_0.click()

# USUÁRIO E SENHA
sleep(1)
login = nav.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
login.send_keys(username)

senha = nav.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")
senha.send_keys(password)

botao_2 = nav.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
botao_2.click()

# TWEET
tweet = nav.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div")
tweet.send_keys(msg)

botao_submit = nav.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]")
botao_submit.click()
