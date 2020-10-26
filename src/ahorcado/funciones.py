import random
import sources as sc

def buscarpalabra(lista):
    ''' Devuelve una palabra aleatoria'''
    numero_random = random.randint(0, len(lista) - 1)
    return lista[numero_random]

def elegirletra ():
    while True : 
        print ('Elige una letra')
        letra = input()
        letra = letra.upper()
        if letra in abecedario:
            return letra
        elif len(letra) != 1:
            print ('Por favor elige una sola letra')
        else:
            print('Esa letra no es posible añadirla, prueba otra vez.')

def otrapartida():
    print('Que bien lo hemos pasado, ¿echamos otra partida? (SI/NO)')
    return input().upper()

'''def comienzaeljuego ():
    letras_verdaderas : []
    letras_incorrectas : []
    fallos = 0
'''
