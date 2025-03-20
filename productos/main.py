from clothes import Ropa
from food import Alimento
from electronic import Electronico

# Función para mostrar el impuesto
def mostrar_impuesto(producto):
    impuesto = producto.calcular_impuesto()
    print(f"Impuesto para {producto.nombre}: ${impuesto:.2f}")  # Formateo a 2 decimales

# Programa principal
if __name__ == "__main__":
    # Crear instancias de las subclases
    telefono = Electronico("Smartphone", 500.00, 12)
    manzana = Alimento("Manzana", 1.50, "2023-12-31")
    camiseta = Ropa("Camiseta", 20.00, "M\n")

    # Mostrar información de los productos
    telefono.mostrar_informacion()
    manzana.mostrar_informacion()
    camiseta.mostrar_informacion()

    #Polimorfismo
    productos = [telefono, manzana, camiseta]
    for producto in productos:
        mostrar_impuesto(producto)
   
       