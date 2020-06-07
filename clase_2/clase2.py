# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    juan = turtle.Turtle()

    make_square(juan)
    turtle.mainloop()

def make_square(juan):
    print("Ingrese el tamaño de la figura: ")
    length = int(input())
    print("Ingrese la cantidad de lados: ")
    n = int(input())

    for i in range(n):
        make_line_and_turn(juan, length,n)

def make_line_and_turn(juan, length,n):
    angle = 360/n
    juan.forward(length)
    juan.left(angle)
    

if __name__ == '__main__':
    main()