#Las tuplas son inmutables, no se pueden cambiar
meses = ("Enero", "Febrero", "Marzo", "...")
diasSemana = ("Lunes", "Martes", "Miercoles", "...")

#Para crear una tupla de un solo elemento
x = (1,)
print(type(x))


#Aunque tbn podemos crearlo de esta manera
numeros = tuple((1,2,3))

#dir, funcionalidades que podemos hacer en este caso con tuple
print(dir(meses))

#Mostrar elemento en concreto
print(x[0])

#Las tuplas aunque no parezcan muy útiles las usamos sin darnos cuenta
coordenadas = {
    (40.4167,-3.7032):"Madrid"
}