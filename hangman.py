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
    print(letra)
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
    # numval = len(valor)
    guion = ''
    for i in range(1, len(valor)):
        guion += '_ '
    print(guion)
    print(valor)
    # print(numRandom)
    letra = comparacionLetra()
    guion = ''
    for i, comp in enumerate(valor):
        print(i, comp)
        if letra != comp:
            if comp == '\n':
                break
            guion += '_ '
            # borrarPantalla()
            # print('llegamos')
            # print(valor.replace(letra, '_'))
            # # time.sleep(2.5)
        #     # # break
        elif letra == comp:
            guion += letra
    print(guion)
    # for i, palab in numPalbras.items():
    #     print(i, palab)
    # time.sleep(4)
    # borrarPantalla()

def run():
    print('¡Adivina la palabra!\n')
    read()
    # comparacionLetra()
    
    


if __name__ == '__main__':
    run()