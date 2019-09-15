#Creamos una función de esta manera:
def hola():
    print("Hello World!")

#De esta manera la invocamos
hola()

#En esta función le estoy indicando que cuando la invoque la voy a llamar con una variable
def nombre(name):
    print("Hello "+ name)
#De estamanera llamo a la función y  le paso el parámtro que requiere mi función nombre
nombre("Joaquín")

#En este caso requiere dos parámetros mi función
def suma (num1, num2):
    return num1 + num2
#Por lo que le paso los dos parámetros necesarios, aunque se pueden crear funciones con valores por defecto
print(suma(1,1))

#Existe una manera más eficiente de crear la función suma, y es la siguiente
#Estoy creando una función con nombre (sumaV2), lambda es para indicar que es una función y los parámetros de esta  es lo anterior a los dos puntos(:), después de los dos puntos es lo que quiero que haga mi función
sumaV2 = lambda num1, num2: num1 + num2
print(sumaV2(10,10))

def resta (num1  = 2, num2 = 3):
    return num1 - num2
