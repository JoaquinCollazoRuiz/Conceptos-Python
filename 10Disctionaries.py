libros = {
    "tipo" : "libro",
    "cantidad" : 1,
    "precio" : 8.99
}

persona = {
    "Nombre" : "Joaquín",
    "Apellido" : "Collazo"
}

print(type(libros))
print(dir(libros))

#Para mostrar solo los keys del diccionario
print(libros.keys())

#Para mostrar todo el contenido, se agrupan por tuplas
print(libros.items())

#Para vaciar el diccionario
persona.clear()

#Podemos crear varios diccionarios dentro de una lista
productos = [
    {"Nombre":"Libro", "precio":8.99},
    {"Nombre":"Manzana", "precio": 0.72}
]
print(productos)