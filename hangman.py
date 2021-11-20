import os
import time
import random

from monito import HANGMANPICS


def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def comparacionLetra():
    try:
        letra = input('Ingrese una letra: ')
        if letra.isnumeric(): 
            raise ValueError('No se pueden ingresar números')
        if len(letra) >= 2:
            raise TypeError('Solo puedes ingresar una letra')
        return letra
    except ValueError as ve:
        print(ve)
        time.sleep(2)
    except TypeError as re:
        print(re)
        time.sleep(2)
    

def trashendo_hangman(vidas):
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
# =========''']

    HANGMANPICS.reverse()
    mono = {}
    for i, val in enumerate(HANGMANPICS, 0):
        mono.setdefault(i, val)
    
    print(mono.get(vidas))
    return ''


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
    vidas = 6
    # print(guion)
    for i in range(0, 100):
        constPal = ''
        # vidasglob -= 1
        letra = comparacionLetra()
        for i, comp in enumerate(valor):
            if letra == comp:
                guion[i] = letra
        if letra not in valor:
             vidas -= 1
        for ele in guion:
            constPal += ele
        if palcomp == constPal:
            borrarPantalla()
            print(constPal)
            print('Ganaste!!')
            break
        borrarPantalla()
        trashendo_hangman(vidas)
        print(constPal)
        if vidas == 0:
            time.sleep(1)
            borrarPantalla()
            print('Perdiste ):\nLa palabra era: ', palcomp)
            time.sleep(2)
            borrarPantalla()
            break
            

def run():
    borrarPantalla()
    print(trashendo_hangman(6))
    print('¡Adivina la palabra!\n')
    read()
    # comparacionLetra()
    
    


if __name__ == '__main__':
    run()