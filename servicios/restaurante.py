from modelos.producto import Producto

class Restaurante:
    """Clase de servicio encargada de administrar los productos del restaurante."""
    
    def __init__(self):
        # Una sola lista para almacenar todos los productos (platillos y bebidas)
        self.lista_productos = []

    def agregar_producto(self, producto: Producto):
        """Añade un objeto de tipo Producto (o sus clases hijas) a la lista."""
        self.lista_productos.append(producto)
        print(f"✔️ Producto '{producto.nombre}' registrado con éxito.")

    def mostrar_restaurante(self):
        """Muestra de manera organizada los datos en consola aplicando Polimorfismo."""
        print("\n" + "="*20 + " MENÚ DEL RESTAURANTE " + "="*20)
        if not self.lista_productos:
            print("No hay productos registrados en este momento.")
        else:
            for producto in self.lista_productos:
                # Polimorfismo: llama automáticamente al método de Platillo o Bebida según corresponda
                print(producto.mostrar_informacion())
        print("="*62)