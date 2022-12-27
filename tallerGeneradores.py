"""Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"] Imprimirlos de la siguiente forma:

Marcelo : 15

José : 20

Juan : 18"""

# notas= [15,20,18]
# alumnos= ["Marcelo", "José", "Juan"]

# # juntar= zip(notas, alumnos)
# for i in zip(alumnos, notas):
#     print(i)

"""Dada la siguiente lista ['Hola', True, 5, 6.04]

Imprimir los valores e índices sin utilizar un contador o range.

0 -> Hola
1 -> True
2 -> 5
3 -> 6.04"""

# lista= ['Hola', True, 5, 6.04]
# for cont, value in enumerate(lista):
#     print(cont, "->", value)

"""Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"], imprimirlos de la siguiente forma:

1 -> Jose : 20

2 -> Juan : 18

3 -> Marcelo : 15
No usar range, ni comparadores. Hint: usar sorted"""

# notas= [20,18,15]
# alumnos= sorted(["Marcelo", "José", "Juan"])


# for cont, value in enumerate(zip(alumnos, notas), start= 1):
#     print(cont, "->", value)

"""Escriba un generador que permita contar las letras de las palabras de una lista.

Ejemplos:

Para "humanidad": {'h': 1, 'u': 1, 'm': 1, 'a': 2, 'n': 1, 'i': 1, 'd': 2}

Para "humano": {'h': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 1, 'o': 1}"""
###SIN USAR FUNCION GENERADORA

word= "humanidad"
palabra= list(word)


elemento= []
for i in word:
    conteo= palabra.count(i)
    elemento.append(conteo)
#print(elemento)

letras= []
for element in palabra:
    letras.append(element)
#print(letras)

zipped= zip(letras, elemento)
#print(zipped)

resultado= []
for n in zipped:
    if n not in resultado:
        resultado.append(n)
print(dict(resultado))

##CON FUNCION GENERADORA:

##LOGICA DE UNA FUNCION NORMAL
def funcion_generadora(lista):
    listaNueva= []
    for palabra in lista:
        diccionario= {}
        for letra in palabra:
            contador= palabra.count(letra)
            diccionario[letra]= contador
        listaNueva.append(diccionario)
    return listaNueva

lista= ["humanidad", "humano"]
print(funcion_generadora(lista))

##TRANSFORMANDO  UNA FUNCION NORMAL A FUNCION GENERADORA
def funcion_generadora(lista):
    #listaNueva= []
    for palabra in lista:
        diccionario= {}
        for letra in palabra:
            contador= palabra.count(letra)
            diccionario[letra]= contador
        #listaNueva.append(diccionario)
    #return listaNueva  
    #return diccionario
        yield diccionario
#COMO LLAMAMOS A UNA FUNCION GENERADORA? USANDO UN FOR

listaPalabras= ["humanidad", "humano"]
for elemento in funcion_generadora(listaPalabras):
    print(elemento)

"""
Teniéndonos los siguientes criterios:

Desaprobado: nota < 11
Destacado: nota > 16
Aprobado: para el resto de casos
notas = [15, 20 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
alumnos_notas = zip(alumnos, notas)

def registrar_aprobados(l):
    pass
Implementar registrar_aprobadoscomo generador y que su único parámetro de entrada sea alumnos_notas Posteriormente utilizar un bucle y 
enumerar para obtener la siguiente salida.

1 -> Marcelo : 15 (Aprobado)
2 -> Jose : 20 (Destacado)
3 -> Juan : 18 (Destacado)
4 -> Marco : 11 (Aprobado)
5 -> María : 4 (Desaprobado)
6 -> Ricardo : 7 (Desaprobado)
7 -> Liz : 14 (Aprobado)
8 -> Diego : 13 (Aprobado)
9 -> Roberto : 1 (Desaprobado)
10 -> Martin : 9 (Desaprobado)
11 -> Álvaro : 10 (Desaprobado)
"""

notas= [15, 20, 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
alumnos_notas = zip(alumnos, notas)

#print(list(alumnos_notas))
##LOGICA DE UNA FUNCION NORMAL
# def registrar_aprobados(l):
#     lista_final= []
#     for alumnos, notas in l:
#         if notas < 11:
#             desaprobados= f"{alumnos}: {notas} (Desaprobado) "
#             lista_final.append(desaprobados)
#         elif notas > 16:
#             destacados= f"{alumnos}: {notas} (Destacado) "
#             lista_final.append(destacados)
#         else:
#             aprobados= f"{alumnos}: {notas} (Aprobado) "
#             lista_final.append(aprobados)
#     return lista_final

#     for num, i in enumerate(lista_final, start= 1):
#         resultados=  f"{num}  -> {i}"
#     return resultados

# print(registrar_aprobados(alumnos_notas))


#TRANSFORMANDOLO EN UNA FUNCION GENERADORA

def registrar_aprobados(l):
    for alumnos, notas in l:
        if notas < 11:
            desaprobados= f"{alumnos}: {notas} (Desaprobado) "
            yield desaprobados
        elif notas > 16:
            destacados= f"{alumnos}: {notas} (Destacado) "
            yield destacados
        else:
            aprobados= f"{alumnos}: {notas} (Aprobado) "
            yield aprobados
    
for numero, element in enumerate(registrar_aprobados(alumnos_notas), start= 1):
    print(f"{numero} -> {element}")
