#input me permite pedirle al usuario que introduza algo y guardarlo en mi variable num1
num1 = input("Introduce un número: ")
print(num1) 
print(type(num1)) #String
print(type(int(num1))) #Int
print(type(float(num1))) #Float
#en este caso num1 es considerado un string, en caso de querer realizar alguna operación debemos convertirlo a int
num2 = 10
print("Su número + 10 = " + int(num1)+num2)