import numpy as np
import nltk
import json
import pprint
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


stemmer = SnowballStemmer("english")
#lectura de stopwords
archivo = open("./stopwords.txt", "r", encoding="utf-8")
contenido = archivo.read()
stoplist = contenido.split()
ropa = []
filtro = []
for x in range(97, 123):
    filtro.append(chr(x))

#lesctura de archivo
def documento(nombre,articulos):
    file = open("archive/"+str(nombre), "r")
    archivo = file.read()
    lista = archivo.split("\n")
    articulos = []
    b = 0
    for linea in lista:
        temp = linea.split(",")
        art = ""
        for i in range(9,len(temp)):
            art += temp[i]
        articulos.append(art)



#preprosesamiento 
def preprocesamiento(texto):
    palabra =""
    prefijos ={}
    i = 0
    index = 0
   #tokenizacion
    for ropa in texto:
        cant = 0
        for letra in ropa:
            letra = letra.lower()
            if letra != "":
                if letra in filtro:
                   palabra += letra 
                else:
                # filtramos los stopwords
                    if len(palabra) >= 3:
                        if palabra not in stoplist and palabra!="":
                        # reducir palabras (stemming)
                            palabra = stemmer.stem(palabra)
                            #creamos un txt para almacenar la palabra reducida y si existe añadirle el index sino existe la palabra la crea en nuevo txt.
                            if palabra not in list(prefijos.keys()):
                                f = open("./keyword/"+str(i)+".txt","w")
                                f.write(palabra + ","+str(index))
                                f.close()
                                prefijos[palabra] = i
                                i += 1   
                                cant +=1      
                            else : 
                                f = open("./keyword/"+str(prefijos[palabra])+".txt","a")
                                f.write(","+str(index))
                                f.close()
                                cant +=1         
                    palabra = "" 
        f = open("./size.txt","a")
        f.write(str(index)+":"+str(cant)+"\n")
        f.close()
        print("Articulo: "+str(index))
        index += 1  
        


preprocesamiento(ropa)

