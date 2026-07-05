from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    # 1. Instanciar el servicio del restaurante
    mi_restaurante = Restaurante()

    print("--- Registrando Productos en el Sistema ---")
    # 2. Crear dos objetos de tipo Platillo y dos de tipo Bebida
    platillo1 = Platillo("Maito de Pescado", 8.50, "Plato Fuerte")
    platillo2 = Platillo("Ceviche de Volquetero", 6.00, "Entrada")
    
    bebida1 = Bebida("Chicha de Chonta", 1.50, 500)
    bebida2 = Bebida("Jugo de Guayusa", 1.25, 400)

    # 3. Prueba de validación de precio negativo (Requisito de la guía)
    print("\n[Prueba de Validación de Encapsulamiento]")
    platillo1.cambiar_precio(-3.50)  # Mostrará un mensaje de error en consola

    # 4. Agregar los objetos a la lista del servicio
    print("\n[Guardando Productos]")
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    # 5. Mostrar los resultados finales (Demostración de Polimorfismo)
    mi_restaurante.mostrar_restaurante()

if __name__ == "__main__":
    main()