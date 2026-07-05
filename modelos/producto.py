# modelos/producto.py

class Producto:
    """Clase padre que representa un producto general del restaurante."""
    
    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        self.nombre = nombre
        # Aplicando encapsulamiento al atributo precio usando un guion bajo (_)
        self._precio = 0.0
        self.cambiar_precio(precio)  # Valida el precio que se ingresa al inicio
        self.disponible = disponible

    # Método de acceso (Getter) para obtener el precio protegido
    def obtener_precio(self) -> float:
        return self._precio

    # Método de modificación (Setter) con la validación requerida
    def cambiar_precio(self, nuevo_precio: float):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print(f"Error: El precio no puede ser negativo ni igual a cero al momento de modificarlo.")

    def mostrar_informacion(self) -> str:
        """Método base para mostrar la información del producto."""
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.obtener_precio():.2f} | Estado: {estado}"