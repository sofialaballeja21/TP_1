class Factorial:
    def __init__(self):
        pass
    
    def calculate_factorial(self, num):
        if num < 0:
            print("El factorial de un número negativo no está definido.")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            return fact
    
    def run(self, min_num, max_num):
        for num in range(min_num, max_num + 1):
            print(f"Factorial de {num} es {self.calculate_factorial(num)}")


if __name__ == "__main__":
    min_num = int(input("Ingresa el número mínimo: "))
    max_num = int(input("Ingresa el número máximo: "))
    
    factorial_obj = Factorial()
    factorial_obj.run(min_num, max_num)
