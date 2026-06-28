# main.py

# Importaciones relativas limpias basadas en una estructura de paquetes válida
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def ejecutar_sistema() -> None:
    # 1. Instanciar el servicio controlador principal
    mi_establecimiento = Restaurante("Amazonía Gourmet")
    
    print("--- INICIANDO CARGA DE DATOS ---")
    
    # 2. Instanciar objetos concretos de los modelos
    platillo_1 = Producto("Maito de Pescado", 12.50, True)
    platillo_2 = Producto("Ceviche de Volquetero", 6.00, True)
    bebida_1 = Producto("Chicha de Chonta", 1.50, False)  # Producto Agotado
    
    usuario_1 = Cliente("1726354819", "Kevin Jiménez", 4)
    usuario_2 = Cliente("0504123987", "María Andrade", 2)
    
    # 3. Registrar los objetos creados dentro de las listas del servicio
    mi_establecimiento.registrar_producto(platillo_1)
    mi_establecimiento.registrar_producto(platillo_2)
    mi_establecimiento.registrar_producto(bebida_1)
    
    mi_establecimiento.registrar_cliente(usuario_1)
    mi_establecimiento.registrar_cliente(usuario_2)
    
    # 4. Presentar toda la información estructurada en consola
    mi_establecimiento.mostrar_informacion_sistema()

if __name__ == "__main__":
    ejecutar_sistema()


   