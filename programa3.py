from selenium import webdriver
mydriver = webdriver.Firefox()

mydriver.get("https://translate.google.com.mx/")
###  la linea anterior, espera a que se termine de cargar la pagina

areaTexto= mydriver.find_element_by_id("source")

print(dir(areaTexto))
areaTexto.send_keys("studing with friends :D !")

##############  PARTE 2  #############

words = [ "dog", "My dog ate my homework", "I love python"]

for i in words:
    areaTexto.clear()  ### primero hay limpiar el text tarea
    areaTexto.send_keys(i)
    input("continuar")
    
input("terminado")
mydriver.close()