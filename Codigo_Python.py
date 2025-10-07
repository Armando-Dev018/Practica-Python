import random

# La computadora elige un número secreto entre 1 y 50
numero_secreto = random.randint(1, 50)
intentos = 0

print("🎲 ¡Adivina el Número! 🎲")
print("He pensado en un número entre 1 y 50. ¿Puedes adivinar cuál es?")

# Bucle principal del juego
while True:
    try:
        # Pedir un número al usuario
        suposicion = int(input("Ingresa tu número: "))
        intentos = intentos + 1 # Incrementar el contador de intentos

        # Comprobar la suposición del usuario
        if suposicion < numero_secreto:
            print("¡Muy bajo! Intenta con un número más grande. ⬆️")
        elif suposicion > numero_secreto:
            print("¡Muy alto! Intenta con un número más pequeño. ⬇️")
        else:
            print(f"🎉 ¡Felicidades! ¡Adivinaste el número en {intentos} intentos! 🎉")
            break # Termina el bucle porque el usuario adivinó
    
    except ValueError:
        print("Error: Eso no es un número. Por favor, intenta de nuevo.")
