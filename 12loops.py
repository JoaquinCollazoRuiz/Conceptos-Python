# coding=utf-8
letras = ["a","b","c","d"]

#De esta manera devuelvo el array entero
for letras in letras:
    print(letras)

#Cuando recorro el array el momento en el que llegue a la letra c parará el bucle
for letras in letras:
    if letras == "c":
        print("Estas en c")
        break

#Con continue lo que hago en este caso es saltarme la letra b
for letras in letras:
    if letras == "b":
        continue
    print(letras)

for numero in range(1,11):
    if numero == 1:
        print("A")
        break
    if numero == 2:
        print("B")
        break
    else:
        print(numero)
        break

for letra in "Joaquin":
    print(letra)


num = 1

#En este bucle una vez entra en el while no deja de hacerse hasta que se cumple la condición
while num <= 7:
    print(num)
    num = num + 1