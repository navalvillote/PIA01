# Escribe un programa que permita al usuario crear dos conjuntos de números
# enteros. Luego, el programa debe calcular y mostrar:
# 1. La intersección de ambos conjuntos (elementos comunes).
# 2. La unión de ambos conjuntos (todos los elementos sin duplicados).
# 3. La diferencia simétrica (elementos que están en uno u otro conjunto,
# pero no en ambos).


#creo una funcion que dandola por parametros los dos conjuntos me devuelva
#la intersección de ambos conjuntos
def intersecion (conjunto1, conjunto2):
    resultado=[]
    for numero in conjunto1:
    #recorro el conjunto1 y compruebo en cada uno de sus valores si se
    #encuentran en el conjunto2, en caso afirmativo lo añado a resultado
        if numero in conjunto2:
            resultado.append(numero)
    return resultado

#creo una funcion que dandola por parametros los dos conjuntos me devuelva
#la unión de ambos conjuntos
def union (conjunto1, conjunto2):
    resultado=conjunto2[:]
    #hago una copia del conjunto2 en el resultado ya que llevara integro
    for numero in conjunto1:
    #recorro el conjunto1 y compruebo en cada uno de sus valores si se
    #encuentran en el conjunto2, en caso negativo lo añado a resultado
        if not numero in conjunto2:
            resultado.append(numero)
    return resultado

#creo una funcion que dandola por parametros los dos conjuntos me devuelva
#la diferencia simetrica de ambos conjuntos
def diferenciaSimetrica (conjunto1, conjunto2):
    resultado=[]
    for numero in conjunto1:
    #recorro el conjunto1 y compruebo en cada uno de sus valores si se
    #encuentran en el conjunto2, en caso negativo lo añado a resultado
        if not numero in conjunto2:
            resultado.append(numero)
    for numero in conjunto2:
    #recorro el conjunto2 y compruebo en cada uno de sus valores si se
    #encuentran en el conjunto1, en caso negativo lo añado a resultado
        if not numero in conjunto1:
            resultado.append(numero)
    return resultado

#asigno una serie de valores aleatorios a cada conjunto
conjunto1=[1, 4, 8, 3, 7]
conjunto2=[9, 8, 3, 5, 1]

#calculamos el resultado de cada uno de los apartados
apartado1=intersecion(conjunto1,conjunto2)
apartado2=union(conjunto1,conjunto2)
apartado3=diferenciaSimetrica(conjunto1,conjunto2)

#mostramos los resultados por pantalla
print (f'La intersección es: {apartado1}')
print (f'La unión es: {apartado2}')
print (f'La difernecia simétrica es: {apartado3}')