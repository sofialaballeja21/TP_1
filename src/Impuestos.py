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