import time
import pyautogui

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico)

navegador.get("https://freebitco.in/signup/?op=s")
navegador.maximize_window()
time.sleep(3)

#LOGIN INICIAR
navegador.find_element(By.XPATH, '/html/body/div[2]/div/nav/section/ul/li[10]/a' ).click()

time.sleep(2)

navegador.find_element(By.XPATH, '//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]' ).click()
#CAMPO LOGIN
navegador.find_element(By.XPATH, '//*[@id="login_form_btc_address"]' ).send_keys("email@gmail.com")

time.sleep(2)
#CAMPO SENHA
navegador.find_element(By.XPATH, '//*[@id="login_form_password"]' ).send_keys("senhalogin")

time.sleep(2)
#BOTAO DE LOGIN
navegador.find_element(By.XPATH, '//*[@id="login_button"]' ).click()

time.sleep(5)

navegador.maximize_window()

#SEGUNDO AVISO NO THANKS
navegador.find_element(By.XPATH, '//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]' ).click()

time.sleep(5)

pyautogui.click(x=1909, y=925)

time.sleep(5)

#Caixa Preencher
#Altere as configurações de pixel para conseguir clicar na caixa preencher
pyautogui.click(x=831, y=785)

time.sleep(30)
'''
#BOTAO ROLL
navegador.find_element(By.XPATH, '//*[@id="free_play_form_button"]' ).click()

time.sleep(5)
'''

        #x=1909, y=925          #x=831, y=785
