#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) < 2:
    range_input = input("Por favor, ingresa el rango (desde-hasta) para calcular los factoriales: ")
    start, end = map(int, range_input.split("-"))
else:
    range_input = sys.argv[1]
    start, end = map(int, range_input.split("-"))

for num in range(start, end+1):
    print("Factorial", num, "! es", factorial(num))



