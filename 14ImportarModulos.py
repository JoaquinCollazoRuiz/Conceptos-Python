#Las mejores páginas sobre documentación de librerias son:
# https://docs.python.org/3/library/index.html#library-index
# https://pypi.org/

#La manera de importar un módulo es
import datetime
#Y de esta manera podemos usar funciones que nos proporciona este módulo
print(datetime.date.today())

#Aunque tbn lo puedes importar de esta manera
from datetime import timedelta, date
#El porque hacer esto es porque de esta manera si quieres usar algo concreto necesitas menos código a la hora de invocarlo
print(date.today())

#De esta manera llamas a tu propio módulo
import miModuloSuma_15
#De esta manera puedo llamar a mi función y utilizarla desde esta clase
miModuloSuma_15.suma(1,1)
