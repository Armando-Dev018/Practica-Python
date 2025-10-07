# --- Definición de Funciones para cada operación ---
def sumar(a, b):
    """Esta función toma dos números y devuelve su suma."""
    return a + b

def restar(a, b):
    """Esta función toma dos números y devuelve su resta."""
    return a - b

def multiplicar(a, b):
    """Esta función toma dos números y devuelve su multiplicación."""
    return a * b

def dividir(a, b):
    """
    Esta función toma dos números y devuelve su división.
    Maneja el error de división por cero.
    """
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

# --- Bucle principal del programa ---
while True:
    # Mostrar el menú de opciones
    print("\n--- Calculadora Básica ---")
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    # Pedir la opción al usuario
    opcion = input("Ingresa el número de la opción (1/2/3/4/5): ")

    # Salir del bucle si el usuario elige la opción 5
    if opcion == '5':
        print("¡Adios! 👋")
        break

    # Validar que la opción sea una de las permitidas
    if opcion in ('1', '2', '3', '4'):
        try:
            # Pedir los números y convertirlos a float
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            # Manejar el error si el usuario no ingresa un número
            print("Error: Por favor, ingresa solo valores numéricos.")
            continue # Vuelve al inicio del bucle

        # Realizar la operación según la opción elegida
        if opcion == '1':
            resultado = sumar(num1, num2)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == '2':
            resultado = restar(num1, num2)
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == '4':
            resultado = dividir(num1, num2)
            print(f"El resultado de la división es: {resultado}")
    else:
        # Mensaje para opciones no válidas
        print("Opción no válida. Por favor, elige un número del 1 al 5.")