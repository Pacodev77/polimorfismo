from producto import Producto

# Subclase Electrónico
class Electronico(Producto):
    def __init__(self, nombre, precio, garantia_meses):
        super().__init__(nombre, precio)
        self.garantia_meses = garantia_meses

    # Implementación del método abstracto
    def calcular_impuesto(self):
        return self.precio * 0.15  # Impuesto del 15% para productos electrónicos

    # Sobrescritura del método mostrar_informacion
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Garantía: {self.garantia_meses} meses")

