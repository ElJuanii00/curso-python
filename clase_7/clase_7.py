# -*- coding: utf-8 -*-

import os

def compare2strings(result):
    if result is True:
        print('{} si es un palindromo'.format(word))
    else:
        print('{} no es un palindromo'.format(word))


def palindrome2(word):
    reversed_letters = word[::-1]
    
    if reversed_letters == word:
        return True
    return False

def palindrome1(word):
    reversed_letters = []
    
    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True
    return False

if __name__ == "__main__":
    val = False

    while not (val):
        programa = int(input('1) Programa estandar, 2) Programa bufircado\n'))
        os.system('clear')
        word = str(input("Escriba la palabra: \n"))
        if(programa == 1):
            result = palindrome1(word)
            compare2strings(result)
            val = True
        elif(programa == 2):
            result = palindrome2(word)
            compare2strings(result)
            val = True
        else:
            print("opcion incorrecta")
