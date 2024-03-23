# Los números van desde 1 hasta 100
lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")
#imprime los numeros primos entre 1 y 100

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num) 
           
#comentario de prueba para actualizar en GitHub
#
#
#
