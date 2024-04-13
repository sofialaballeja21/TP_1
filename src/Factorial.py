#Punto 1
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

#Punto 2
class CalculadoraImpuestos:
    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones_municipales = base_imponible * 0.012
        
        total_impuestos = iva + iibb + contribuciones_municipales
        
        return total_impuestos

# Ejemplo de uso
calculadora = CalculadoraImpuestos()
importe_base_imponible = 1000  # Ejemplo de un importe base imponible de 1000
impuestos_calculados = calculadora.calcular_impuestos(importe_base_imponible)
print("Total de impuestos a pagar:", impuestos_calculados)

#Punto 3
class Hamburguesa:
    def __init__(self, tipo):
        self.tipo = tipo
        
    def mostrador(self):
        print(f'La hamburguesa {self.tipo} se retirara por mostrador')
    
    def retira_cliente(self):
        print(f'La hamburguesa {self.tipo} la retira el cliente')
        
    def entrega_domiclio(self):
        print(f'La hamburguesa {self.tipo} se entrega a domicilio')
        
hamburguesa = Hamburguesa('Completa')
hamburguesa.entrega_domiclio()
hamburguesa.mostrador()
hamburguesa.entrega_domiclio()

#Punto 4
class Factura:
    def __init__(self, importe, condicion_impositiva):
        self.importe = importe
        self.condicion_impositiva = condicion_impositiva

    def generar_factura(self):
        if self.condicion_impositiva == "IVA Responsable":
            impuesto = self.importe * 0.21
            total = self.importe + impuesto
            return f'Factura con IVA Responsable: Importe total: ${total:.2f} (IVA: ${impuesto:.2f})'
        elif self.condicion_impositiva == 'IVA No inscripto':
            return f'Factura con IVA No Inscripto: Importe total ${self.importe:.2f}'
        elif self.condicion_impositiva == "IVA Exento":
            return f"Factura con IVA Exento: Importe total ${self.importe:.2f}"
        else:
            return "Condición impositiva no reconocida"

# Ejemplo de uso
factura1 = Factura(1000, "IVA Responsable")
print(factura1.generar_factura())

factura2 = Factura(800, "IVA No Inscripto")
print(factura2.generar_factura())

factura3 = Factura(1200, "IVA Exento")
print(factura3.generar_factura())

#Punto 5
def getAvion(self):
      avion = Avion()
      
      bodyA = self.__builder.getBodyA()
      avion.setBodyA(bodyA)
      
      #Turbina 2
      i = 0
      while i < 4:
        turbina = self.__builder.getTurbina()
        avion.attachTurbina(turbina)
        i += 1
        
      #Alas 2
      i = 0
      while i < 4:
        alas = self.__builder.getAlas()
        avion.attachAlas(alas)
        i += 1
      
      #Tren de Aterrizaje
      trenAterrizaje = self.__builder.getTrenAaterrizaje()
      avion.setTrenAaterrizaje(trenAterrizaje)
#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Avion:
   def __init__(self):
      self.__turbina = list()
      self.__alas = None
      self.__bodyA = None
      self.__trenAterrizaje = None

   def setBodyA(self, bodyA):
      self.__bodyA = bodyA

   def attachTurbia(self, turbina):
      self.__turbina.append(turbina)

   def setAlas(self, alas):
      self.__alas = alas
      
   def setTrenAterrizaje(self, trenAterrizaje):
      self.__trenAterrizaje = trenAterrizaje

   def specification(self):
      print ("chasis: %s" % (self.__bodyA.shape))
      print ("Alas: %d" % (self.__alas.horsepower))
      print ("Turbina: %d\'" % (self.__turbina[0].size))
   