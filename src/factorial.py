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
else:
    range_input = sys.argv[1]
    
if "-" not in range_input:
    print("El formato del rango es incorrecto. Debe ser 'desde-hasta'.")
    sys.exit()

start, end = map(int, range_input.split("-"))
start = int(start) if start else 1
end = int(end) if end else 60

if start <= 0 or end <= 0:
    print("Los números negativos no son válidos.")
    sys.exit()

if start > end:
    print("El número de inicio debe ser menor o igual que el número final.")
    sys.exit()

for num in range(start, end+1):
    print("Factorial", num, "! es", factorial(num))



