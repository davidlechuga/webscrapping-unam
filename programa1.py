from selenium import webdriver
from selenium.webdriver.common.keys import Keys

busqueda = input("Que deseas buscar [     ]  ")

browser = webdriver.Firefox()

browser.get("https://www.google.com.mx/")
barraBus= browser.find_element_by_name("q")

barraBus.send_keys(busqueda)

barraBus.send_keys(Keys.ENTER)
