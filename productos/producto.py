from abc import ABC, abstractmethod

# Clase abstracta Producto
class Producto(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Método abstracto que debe ser implementado por las subclases
    @abstractmethod
    def calcular_impuesto(self):
        pass

    # Método común para mostrar la información del producto
    def mostrar_informacion(self):
        print(f"\nNombre: {self.nombre}, Precio: ${self.precio:.2f}")

