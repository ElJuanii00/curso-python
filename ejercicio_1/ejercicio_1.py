# -*- coding: utf-8 -*-

import os

def finder(word,letter):
    for length in word:
        print(length)
        if length == letter:
                print("Lawa letra {} fue encontrada en {}".format(length, word))
                return True
        else:
                return False


def main():
    word = str(input("Escribe una palabra:\n"))
    os.system('clear')
    letter = str(input("Escribe la letra que deseas buscar:\n"))
    os.system('clear')
    finder(word,letter)

if __name__ == "__main__":
    main()