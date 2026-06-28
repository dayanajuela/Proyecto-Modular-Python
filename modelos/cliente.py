# modelos/cliente.py

class Cliente:
    """Clase que representa un cliente registrado en el restaurante."""
    
    def __init__(self, cedula: str, nombre_completo: str, mesa_asignada: int):
        # Atributos con tipos explícitos para cumplir con la rúbrica
        self.cedula: str = cedula
        self.nombre_completo: str = nombre_completo
        self.mesa_asignada: int = mesa_asignada

    def __str__(self) -> str:
        # Método especial para dar un formato limpio de texto al objeto
        return f"Cliente: {self.nombre_completo} (C.I: {self.cedula}) | Mesa asignada: {self.mesa_asignada}"