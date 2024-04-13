'''Provea una clase que dado un número entero cualquiera retorne el factorial del 
mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma 
instancia de clase.'''
class Factorial:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._result_cache = {}  # Cache para almacenar resultados previamente calculados
        return cls._instance

    def calcular_factorial(self, nro):
        if nro < 0:
            raise ValueError("El factorial no está definido para números negativos")
        if nro in self._result_cache:
            return self._result_cache[nro]  # Devuelve el resultado previamente calculado si está en caché
        if nro == 0:
            return 1
        else:
            resultado = nro * self.calcular_factorial(nro - 1)
            self._result_cache[nro] = resultado  # Almacena el resultado en caché para uso futuro
            return resultado

# Ejemplo de uso
factorial_calculator = Factorial()

# Se puede invocar desde cualquier lugar de la aplicación utilizando la misma instancia
resultado_5 = factorial_calculator.calcular_factorial(5)
print(resultado_5)  # Salida: 120

resultado_3 = factorial_calculator.calcular_factorial(3)
print(resultado_3)  # Salida: 6


'''EXTENSION DE PROTOTYPE'''
import copy
import time


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


def simulate_processing():
    # Simulate processing time of 2 seconds
    time.sleep(2)


if __name__ == "__main__":
    # Crear instancia inicial de SomeComponent
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    # Crear 20 anidamientos
    for _ in range(20):
        component = copy.deepcopy(component)
        simulate_processing()

    print("Proceso completado.")