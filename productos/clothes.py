from producto import Producto

# Subclase Ropa
class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    # Implementación de la abstraccion
    def calcular_impuesto(self):
        return self.precio * 0.10  

    # Sobrescritura del método mostrar_informacion
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Talla: {self.talla}")

#  Polimorfismo
def mostrar_impuesto(producto):
    print(f"El impuesto de {producto.nombre} es: ${producto.calcular_impuesto():.2f}\n")