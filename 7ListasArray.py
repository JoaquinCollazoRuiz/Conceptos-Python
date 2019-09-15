popurri = [1, "A", 2.22, False, [1,2,3,4,5]]
letras = ["A", "B", "C"]
numeros = [1,2,3]

#list nos permite agrupar lo que queramos en una misma varibale similar a un array pero esta todo en el mismo "hueco"
listaNumeros = list((1,2,3,4,5))
print(listaNumeros)

#range me permite crear una lista partiendo del valor 1 hasta el valor 100-1
rangoNumeros = list(range(1 , 100))
print(rangoNumeros)

#Recordar que dir me muestra información acerca de lo que puedo hacer con él
print(dir(numeros))
#Algunas cosas que puedo hacer...
print(popurri[2])
#De esta manera puedo comprobar si mi array contiene 1, devuelve un booleano
print(1 in  popurri)
print("A" in numeros)

#La manera de modificar algún valor del array
print(numeros)
numeros[0] = 0
numeros[1] = 1
numeros[2] = 2
print(numeros)

#Me añade al final el valor D
letras.append("D") 
#La manera de añadir varios valores a la vez
letras.extend(["E","F"])
print(letras)

#Añadir un valor en medio del array y no al final
letras.insert(1, ["A.v2"])
print(letras)
#Eliminar el último elemento del array
letras.pop()
print(letras)
#Eliminar algo concretro
letras.remove("A.v2")
print(letras)
#Vaciar completamente el array
letras.clear()
print(letras) 

#Ordenar un array alfabéticamente
palabras = ["Hola", "Mar", "Que", "Si", "No", "Zeta"]
palabras.sort()
#En caso de querer ordenarlos de manera contraria alfabéticamente
palabras.sort(reverse=True)

#Saber la posición de alguno de mis valores
print(palabras.index("Mar"))

#Cuantas veces aparece un valor en mi array
print(palabras.count("Si"))