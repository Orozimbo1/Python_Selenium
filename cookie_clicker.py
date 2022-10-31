from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class CookieCliker:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
        self.SITE_MAP = {
            "buttons": {
                "upgrade": {
                    "xpath": "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[$$NUMBER$$]"
                }
            }
        }

        self.driver = webdriver.Chrome(executable_path="C:\chromedriver")
        self.driver.maximize_window()

    def abrir_site(self):
        print('oi')
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(8)
        print('oi')

    def selecionar_idioma(self):
        self.driver.find_element(By.ID, 'langSelect-PT-BR').click()
        time.sleep(4)

    def clicar_no_cookie(self):
        self.driver.find_element(By.ID, 'bigCookie').click()

    def pegar_melhor_upgrade(self):
        encontrei = False
        elemento_atual = 2

        while not encontrei:
            objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(elemento_atual))
            classes_objeto = self.driver.find_element(By.XPATH, objeto).get_attribute("class")

            if not "enable" in classes_objeto:
                encontrei = True
            else:
                elemento_atual += 1
        return elemento_atual - 1

    def comprar_upgrade(self):
        
        objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(self.pegar_melhor_upgrade()))
        self.driver.find_element(By.XPATH, objeto).click()


biscoito = CookieCliker()
biscoito.abrir_site()
biscoito.selecionar_idioma()

i = 0

while True:
    if i % 100 == 0 and i != 0:
        time.sleep(1)
        biscoito.comprar_upgrade()
        time.sleep(1)
    biscoito.clicar_no_cookie()
    i += 1