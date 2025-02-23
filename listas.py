##Ejercicio 1 
lista = [1, 2, 3, 4]
if len (lista) == len(set(lista)):
    print("no hay repeticiones")
else:
    print("si hay repeticiones")

##Ejercicio 2
lista_de_cadenas = ["anilina", "hola", "oso", "mundo", "reconocer", "python"]
encontrado = False
for cadena in lista_de_cadenas:
    if cadena == cadena[::-1]:
        print(f"Cadena palíndroma encontrada: {cadena}")
        encontrado = True
if not encontrado:
    print("No existe")

##Ejercicio 3
def tiene_dos_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = sum(1 for letra in cadena if letra in vocales)
    return contador >= 2

lista = ["hola", "casa", "sol", "luz"]

resultado = next((palabra for palabra in lista if tiene_dos_vocales(palabra)), "No existe")
print(resultado)

##Ejercicio 4
def es_palindromo(lista):
    return lista == lista[::-1]

lista = [1, 2, 3, 2, 1]

if es_palindromo(lista):
    print("La lista es un palíndromo")
else:
    print("La lista no es un palíndromo")
