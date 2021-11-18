import os
import time
import random


def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def comparacionLetra():
    letra = input('Ingrese una letra: ')
    letra = letra
    # print(letra)
    return letra


def read():
    palabras = []
    with open('./archivos/palabras.txt', 'r') as f:
        for line in f:
            palabras.append(line) 

    numPalbras = {}
    for i, palabra in enumerate(palabras, 1):
        numPalbras.setdefault(i, palabra)
    
    numRandom = random.randint(1,100)
    valor = numPalbras.get(numRandom)
    valor = valor.lower()

    palcomp = valor
    palcomp = palcomp.replace('\n', '')

    # print(valor)
    # print(palcomp)

    valor = list(valor)
    guion = ['_ '  for i in range (1, len(valor))]

    impguion = ''
    for ele in guion:
        impguion += ele
    print(impguion)
    vidas = 10 
    vidasglob = 10
    # print(guion)
    for i in range(0, vidas):
        constPal = ''
        vidasglob = vidasglob - 1
        letra = comparacionLetra()
        for i, comp in enumerate(valor):
            if letra == comp:
                guion[i] = letra
        for ele in guion:
            constPal += ele
        if palcomp == constPal:
            borrarPantalla()
            print(constPal)
            print('Ganaste!!')
            #break
        borrarPantalla()
        print(constPal)
    if vidasglob == 0:
        borrarPantalla()
        print('Perdiste ):')
        

def run():
    print('¡Adivina la palabra!\n')
    read()
    # comparacionLetra()
    
    


if __name__ == '__main__':
    run()