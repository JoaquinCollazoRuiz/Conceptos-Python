# coding=utf-8
#Para instalar librerias no nativas debo de correr este comando en terminal
# pip install requests

#Para poder instalar un módulo externo de python (con pip), antes debo instalarlo con estos comandos(macos);
# sudo easy_install pip
# sudo pip install --upgrade pip

#De esta manera ya podemos importar librearias externas no nativas de python
#En terminal: pip install requests
import requests

#Petición get
rGet = requests.get('https://www.google.es/')
print(rGet)

#Petición post
url = 'https://www.google.es/'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

rPost = requests.post(url, data=payload, headers=headers)
print(rPost)