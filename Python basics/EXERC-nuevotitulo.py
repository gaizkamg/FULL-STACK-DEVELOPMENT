'''
Dado el siguiente string.

Title: 'Nuevo ejercicio'

Desarrolla un programa en Python que permita generar un nuevo string con todos los caracteres después de los dos puntos (:). El programa deberá imprimir en consola el nuevo string.

Ejemplo.

python main.py
'Nuevo ejercicio'

'''

def string_strip():
    titulo = "Title: 'Nuevo ejercicio'"
    nuevo_string = titulo.lstrip('Title:')
    return print(nuevo_string)

string_strip()


