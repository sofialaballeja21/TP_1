import matplotlib.pyplot as plt

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

x_values = []  # Lista para almacenar el número inicial de la secuencia
y_values = []  # Lista para almacenar el número de iteraciones para converger

for num in range(1, 10001):
    x_values.append(num)
    y_values.append(collatz(num))

plt.figure(figsize=(10, 6))
plt.scatter(y_values, x_values, s=5, color='blue')
plt.title('Convergencia de la conjetura de Collatz para números entre 1 y 10000')
plt.xlabel('Número de iteraciones para converger')
plt.ylabel('Número inicial de la secuencia')
plt.grid(True)
plt.show()

