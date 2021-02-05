#Intento de abrir un archivo HTML local son selenium para hacer scrapping.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import codecs
import os 

def ObtenListaMiembros(nombreArchivo):
    #Obtenemos el directorio del archivo HTML
    directorioArchivo = os.path.dirname(os.path.realpath(nombreArchivo))
    #Juntamos el directorio del archivo y el nombre para formar una URL para poder abrirla con webdriver.Firefox()
    direccionArchivoURL = directorioArchivo + "\\" + nombreArchivo

    #Abrimos Firefox(). Con el get le decimos que abra directamente el navegador con esa URL del archivo.
    driver = webdriver.Firefox()
    driver.get(direccionArchivoURL)

    #Buscamos por xpath los bloques que tienen los correos electrónicos. Todos los enlaces que estén dentro del bloque div con clase especificada.
    listaMiembrosClase = driver.find_elements_by_xpath("//div[@class='CWWGvd']/a")

    #Esto nos devuelve una lista de elementos con propiedades. Dentro de esas propiedades, la que nos interesa se llama "text" pero viene con algunos campos vacíos.
    listaMiembrosClaseLimpia = []
    listaMiembrosClaseLimpia = LimpiaElementosVaciosLista(listaMiembrosClase)

    return listaMiembrosClaseLimpia


def LimpiaElementosVaciosLista(listaMiembrosClase):

    #Creamos una lista auxiliar en la que ir metiendo los elementos que tengan texto
    listaMiembrosClaseLimpia = []

    #Filtramos por la propiedad text
    for i in listaMiembrosClase:
        if(i.text != ""):
            listaMiembrosClaseLimpia.append(i.text)
    

    #Devolvemos la lista limpia con todos los correos
    return listaMiembrosClaseLimpia



#nombreArchivo = "listaMiembros.html"

print(ObtenListaMiembros("listaMiembros0.html"))