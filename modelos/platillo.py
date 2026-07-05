from modelos.producto import Producto

class Platillo(Producto):
    """Clase hija que representa una comida o plato del restaurante."""
    
    def __init__(self, nombre: str, precio: float, tipo_de_platillo: str, disponible: bool = True):
        # Utilizar super() para reutilizar los atributos de la clase padre
        super().__init__(nombre, precio, disponible)
        self.tipo_de_platillo = tipo_de_platillo  # Atributo propio (ej. Entrada, Fuerte, Postre)

    # Sobrescribir el método mostrar_informacion() (Polimorfismo)
    def mostrar_informacion(self) -> str:
        info_padre = super().mostrar_informacion()
        return f"{info_padre} | Tipo: {self.tipo_de_platillo}"