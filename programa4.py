from selenium import webdriver

from time import sleep

mydriver = webdriver.Firefox() ###  utilizar firefox y herramientas

mydriver.get("https://docs.google.com/forms/d/e/1FAIpQLSeoBnLXUBlQXlC_H2gQAlbuO9d6k42oYBdhB3NiH3rXM6Yagw/viewform")  ##  obtener la pagina donde esta el textarea


botones = mydriver.find_elements_by_class_name("freebirdFormviewerViewItemsRadioOptionContainer")  ### obtener los botones

for i in botones: 
    if i.text == "Si":
        i.click()
        sleep(2)

texto = mydriver.find_element_by_name("entry.1939522088")  ## definimiendo nuestra entrada de texto
texto.send._keys("Hola  desde python")
sleep(2)
botonSalir = mydriver.find_element_by_class_name("quantumWizButtonPaperbuttonContent")
botonSalir.click()   ###  guarda el objeto y a este objeto le implementa metodo click.ArithmeticError
input("programaTerminado")
mydriver.close()
