import random

letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "#@!?-_"

unir = f'{letras}{numeros}{simbolos}'
longitud = 10
password = random.sample(unir, longitud)
password_1 = "".join(password)

print(password_1)
