# coding=utf-8
algo = "Hello world"
#dir: me muestra todo lo que soy capaz de hacer con este string
print(dir(algo))

#Una de las funciones que me muestra el dir es upper
#upper me permite combertir el string en mayusc
print(algo.upper())

#lower todo minusc
print(algo.lower())

#swapcase me cambia entre mayusc y minusc las letras
print(algo.swapcase())

#replace remplaza el valor de una de las palabras del string por otra (En este caso convierto el Hello por Bye, por lo que algo seria Bye world)
algo.replace("Hello","Bye")
print(algo.replace("Hello","Bye").upper())
print(algo)

#count, cuantas veces estas usan "x" carácter
print(algo.count("l"))

#startsWith, me permite saber si empieza por el valor indicado(devuelve booleano)
print(algo.startswith("Hello"))

#split, me separa un valor en blanco conviertiendolo en array
print(algo.split())
#Peor tbn puedes hacer que separe por un carácter o algo concreto
print(algo.split("o"))