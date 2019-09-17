# coding=utf-8
colores = {"Rojo", "Azul", "Negro"}

print(colores)
print("Blanco" in colores)
#En este caso en los set la función add añade al inicio del todo
colores.add("Blanco")
print("Blanco" in colores)
#Eliminamos el string Azul
colores.remove("Azul")
#Eliminamos completamente no solo el contenido si no que el set completo
del colores