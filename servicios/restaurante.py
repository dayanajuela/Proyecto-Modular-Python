# servicios/restaurante.py

from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase de servicio encargada de gestionar los flujos de listas del sistema."""
    
    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento: str = nombre_establecimiento
        # Uso obligatorio de listas como tipos de datos compuestos
        self.lista_productos: List[Producto] = []
        self.lista_clientes: List[Cliente] = []

    def registrar_producto(self, producto: Producto) -> None:
        """Añade una instancia de Producto a la lista administrada."""
        self.lista_productos.append(producto)
        print(f"[Sistema] Producto '{producto.nombre}' añadido con éxito.")

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Añade una instancia de Cliente a la lista administrada."""
        self.lista_clientes.append(cliente)
        print(f"[Sistema] Cliente '{cliente.nombre_completo}' registrado.")

    def mostrar_informacion_sistema(self) -> None:
        """Muestra de manera organizada los datos en consola."""
        print(f"\n=========================================")
        print(f" REPORTES DE: {self.nombre_establecimiento.upper()}")
        print(f"=========================================")
        
        print("\n--- MENÚ DEL ESTABLECIMIENTO ---")
        if not self.lista_productos:
            print("No existen productos en el menú.")
        for prod in self.lista_productos:
            print(prod)
            
        print("\n--- CLIENTES ACTUALES EN SALA ---")
        if not self.lista_clientes:
            print("No existen clientes registrados.")
        for cli in self.lista_clientes:
            print(cli)
           