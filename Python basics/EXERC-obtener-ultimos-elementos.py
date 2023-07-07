'''
Dada una lista de una n cantidad de elementos.

[1, 4, 55, True, False. 'PyWombat', False, False, 12, 100, ...]

Desarrolla una función que nos permita conocer los últimos elementos de la lista.

    La función debe tener por nombre last_elements.
    La función debe recibir como argumento (De forma obligatoria) una lista de longitud n.
    La función debe recibir como argumento (De forma obligatoria) la cantidad de elementos a retornar.
    El usuario podrás hacer el llamado de la función pasando como argumento la lista y la n cantidad de últimos elementos a obtener.
    La función deberá retornar una tupla con los últimos n elementos de la lista.

Ejemplo.

>>> last_elements([1, 2, 3, 4, 5, 6 ],  2)
(5, 6)

>>> last_elements([True, True, False, False, True ],  3)
False, False, True

>>> last_elements(['PyWombat', 'Article', 'Ben'],  1)
Ben


'''

def last_elements(lista, elementos):
     return  tuple(lista[-(elementos):])


print(last_elements(['camion', 'coche', 'bicicleta', 'moto', 'tren', 'barco'], 4))