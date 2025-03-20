#Modulo food.py by Paco Ruiz

from producto import Producto

# Metodo de Herencia
class Alimento(Producto):
    def __init__(self, nombre, precio, fecha_caducidad):
        super().__init__(nombre, precio)
        self.fecha_caducidad = fecha_caducidad

    #Metodo de Abstraccion
    def calcular_impuesto(self):
        return self.precio * 0.5
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'fecha de Caducidad: {self.fecha_caducidad}')


















'''from producto import Producto

# Subclase Alimento
class Alimento(Producto):
    def __init__(self, nombre, precio, fecha_caducidad):
        super().__init__(nombre, precio)
        self.fecha_caducidad = fecha_caducidad

    # Implementación del método abstracto
    def calcular_impuesto(self):
        return self.precio * 0.05  # Impuesto del 5% para alimentos

    # Sobrescritura del método mostrar_informacion
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Fecha de caducidad: {self.fecha_caducidad}")'''



    
        

   