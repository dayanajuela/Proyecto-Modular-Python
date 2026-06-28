# modelos/producto.py

class Producto:
    """Clase que representa un plato, bebida o producto disponible en el restaurante."""
    
    def __init__(self, nombre: str, precio: float, disponible: bool):
        # Las asignaciones DEBEN ir aquí adentro, bien alineadas con tabulación
        self.nombre: str = nombre
        self.precio: float = precio
        self.disponible: bool = disponible

    def __str__(self) -> str:
        # Método especial para retornar el estado del producto de forma clara
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Estado: {estado}"
  