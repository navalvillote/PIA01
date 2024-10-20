#Escribe una función que reciba por parámetro una lista de enteros y devuelva
#dos listas: una con los valores negativos que tuviera y otra con los positivos.
#Ambas listas deben estar ordenadas ascendentemente


# Defino la funcion a la que recibirá por parámetro un array llamado lista y devolvera dos
# arrays, uno con los numeros positivos y otro con los numeros negativos
def positivosNegativos(lista):
    #definire dos arrays, uno para los numeros positivos y otro para los numeros negativos
    positivos = []  
    negativos = []

    for numero in lista: #recorro la lista numero a numero
        if numero < 0:
            negativos.append(numero) #en el caso de ser negativo lo añado a negativos
        else:
            positivos.append(numero) #en el caso contrario lo añado a positivos
    #ordeno los arrays resultantes de forma ascendente
    negativos.sort()
    positivos.sort()
    #si quisiera ordenarlos descendentemente tendria que poner array.sort(reverse=True)
    return positivos,negativos #devuelvo los arrays ordenados

#Ejemplo de ejecución
numeros = [7,-1,5,1,-8,-12,-13,0]
#llamo a la función
positivos,negativos=positivosNegativos(numeros)
#muestro por pantalla ambas listas
print("La lista de números positivos es: ",positivos) #saldría: [0, 1, 5, 7]
print("La lista de números negativos es: ",negativos) #saldría: [-13, -12, -8, -1]