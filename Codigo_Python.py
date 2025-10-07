def mostrar_tareas(tareas):
    """Muestra todas las tareas de la lista con su número."""
    print("\n--- Tus Tareas Pendientes ---")
    if not tareas: # Revisa si la lista está vacía
        print("¡No tienes tareas pendientes! ✨")
    else:
        # enumerate nos da el índice (empezando en 1) y el valor de cada item
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")
    print("--------------------------")

def agregar_tarea(tareas):
    """Pide al usuario una nueva tarea y la añade a la lista."""
    nueva_tarea = input("Escribe la nueva tarea: ")
    tareas.append(nueva_tarea)
    print(f"¡Tarea '{nueva_tarea}' agregada!")

def completar_tarea(tareas):
    """Muestra las tareas y pide al usuario que elija una para eliminarla."""
    mostrar_tareas(tareas)
    if not tareas: # No hacer nada si no hay tareas
        return

    try:
        num_tarea = int(input("Ingresa el número de la tarea a completar: "))
        
        # Validar que el número esté en el rango correcto
        if 1 <= num_tarea <= len(tareas):
            # Los índices de la lista empiezan en 0, por eso restamos 1
            indice = num_tarea - 1
            tarea_completada = tareas.pop(indice)
            print(f"✅ ¡Tarea '{tarea_completada}' completada y eliminada!")
        else:
            print("Error: Ese número de tarea no existe.")
    except ValueError:
        print("Error: Por favor, ingresa solo un número.")

# --- Programa Principal ---
# Aquí se inicializa la lista que guardará las tareas
lista_de_tareas = []

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Ver todas las tareas")
    print("2. Agregar una tarea")
    print("3. Completar una tarea")
    print("4. Salir")

    opcion = input("Elige una opción (1/2/3/4): ")

    if opcion == '1':
        mostrar_tareas(lista_de_tareas)
    elif opcion == '2':
        agregar_tarea(lista_de_tareas)
    elif opcion == '3':
        completar_tarea(lista_de_tareas)
    elif opcion == '4':
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")