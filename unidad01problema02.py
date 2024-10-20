# Escribe un programa que pida al usuario ingresar una frase o párrafo. Luego, el
# programa debe contar cuántas veces aparece cada palabra en el texto y mostrar
# las palabras junto con su frecuencia.
# Requisitos:
# 1. Eliminar los signos de puntuación y conver&r todas las palabras a
# minúsculas para evitar diferencias.
# 2. Usar un diccionario donde la clave sea la palabra y el valor sea su
# frecuencia.
# 3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.


import re   # importarmos la libreria re para eliminarde signos de puntuación

def crearDiccionario(parrafo): 
    #creamos una funcion que convierta un parrafo cualquiera en una lista de
    #palabras en minusculas y eliminando los signos de puntuación, convierta
    #la lista en un diccionario con la palabra como clave y la frecuencia 
    #como valor,ordenamos el diccionario por orden alfabetico de la clave 
    #y retornamos el diccionario ya ordenado.

    #pasamos un parrafo ya convertido en minusculas y creamos la lista
    #eliminando los signos de puntuacion.
    palabras=re.findall(r'\w+',parrafo.lower()) 
    diccionario = {}
    for palabra in palabras:
        #para cada palabra que hay en la lista comprobamos si ya esta en el
        #diccionario. En caso de no estar la añadimos y ponemos su frecuencia
        #a 1, de lo contrario sumamos 1 a su frecuencia.
        if palabra in diccionario:
            diccionario[palabra] +=1
        else:
            diccionario[palabra] = 1

    #Ordenamos alfabeticamente el diccionario por su clave.
    diccionario=dict(sorted(diccionario.items()))
    #retornamos el diccionario.
    return diccionario

#asignamos un parrafo a la variable parrafo.
parrafo = """El pequeño perro pequeño quería jugar con la pelota pequeña. 
La pelota pequeña era muy pequeña para el perro pequeño, pero al perro pequeño 
le gustaba mucho la pelota pequeña. El perro pequeño corría y corría con la 
pelota pequeña, pero la pelota pequeña siempre se le escapaba. El perro pequeño 
estaba triste porque no podía atrapar la pelota pequeña."""

#Obtenemos el diccionario del parrafo anterior
diccionario = crearDiccionario(parrafo)

for clave,valor in diccionario.items():
    #Para cada item del diccionario devolveremos su clave y su valor
    #formateado con la palabra y las veces que esta repetida
    if valor==1:
        print(f'La palabra "{clave}" está repetida {valor} vez.')
        #print('La palabra "{}" está repetida "{}" vez.'.format(clave,valor))
        #print("La palabra \"" + clave + "\" está repetida " + str(valor) + " vez.")
    else:
        print(f'La palabra "{clave}" está repetida {valor} veces.')