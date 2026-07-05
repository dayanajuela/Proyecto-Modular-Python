from modelos.producto import Producto

class Bebida(Producto):
    """Clase hija que representa una bebida disponible en el restaurante."""
    
    def __init__(self, nombre: str, precio: float, tamano_ml: int, disponible: bool = True):
        # Utilizar super() para reutilizar los atributos de la clase padre (Producto)
        super().__init__(nombre, precio, disponible)
        self.tamano_ml = tamano_ml  # Atributo propio y específico de la Bebida (en mililitros)

    # Sobrescribir el método mostrar_informacion() (Aplicando Polimorfismo)
    def mostrar_informacion(self) -> str:
        info_padre = super().mostrar_informacion()
        return f"{info_padre} | Tamaño: {self.tamano_ml}ml"