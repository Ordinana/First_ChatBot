import time

nombre = input("Tu nombre porfavor?: ")
print(f"¡¡Hola {nombre}!! Trataré de avergonzarte un poco con unas pequeñas preguntas comprometidas...")
time.sleep(4)

# Pregunta 1 con validación
while True:
    print("\nPregunta 1: ¿Prefieres actividades al aire libre o en interiores?")
    print("1. Al aire libre")
    print("2. En interiores")
    respuesta1 = input("Selecciona 1 o 2: ")
    if respuesta1 == "1" or respuesta1 == "2":
        break  # Entrada válida, salir del bucle
    else:
        print("¡¡Entrada no válida!!. Por favor, selecciona 1 o 2.")

# Pregunta 2 con validación
while True:
    print("\nPregunta 2: ¿Te gusta estar en grupo o solo?")
    print("1. En grupo")
    print("2. Solo")
    respuesta2 = input("Selecciona 1 o 2: ")
    if respuesta2 == "1" or respuesta2 == "2":
        break
    else:
        print("¡¡Entrada no válida!!. Por favor, selecciona 1 o 2.")

# Pregunta 3 con validación
while True:
    print("\nPregunta 3: ¿Prefieres algo activo o relajado?")
    print("1. Activo")
    print("2. Relajado")
    respuesta3 = input("Selecciona 1 o 2: ")
    if respuesta3 == "1" or respuesta3 == "2":
        break
    else:
        print("¡¡Entrada no válida!!. Por favor, selecciona 1 o 2.")

# Pregunta 4 con validación
while True:
    print("\nPregunta 4: ¿Te gusta aprender cosas nuevas?")
    print("1. Sí")
    print("2. No")
    respuesta4 = input("Selecciona 1 o 2: ")
    if respuesta4 == "1" or respuesta4 == "2":
        break
    else:
        print("¡¡Entrada no válida!!. Por favor, selecciona 1 o 2.")

# Pregunta 5 con validación
while True:
    print("\nPregunta 5: ¿Tienes mucho tiempo libre?")
    print("1. Sí")
    print("2. No")
    respuesta5 = input("Selecciona 1 o 2: ")
    if respuesta5 == "1" or respuesta5 == "2":
        break
    else:
        print("¡¡Entrada no válida!!. Por favor, selecciona 1 o 2.")

print("\nProcesando recomendación", end='', flush=True)

for i in range(5):
    time.sleep(1)
    print(".", end='', flush=True)

print("\n")

if respuesta1 == "1" and respuesta2 == "1" and respuesta3 == "1" and respuesta4 == "1" and respuesta5 == "1":
    print("Te recomendamos unirte a un club de senderismo.")
elif respuesta1 == "1" and respuesta2 == "2" and respuesta3 == "1" and respuesta4 == "1" and respuesta5 == "1":
    print("Te recomendamos practicar deportes individuales al aire libre, como correr o ciclismo.")
elif respuesta1 == "2" and respuesta2 == "1" and respuesta3 == "2" and respuesta4 == "1" and respuesta5 == "2":
    print("Podrías disfrutar asistiendo a talleres o clases en grupo.")
elif respuesta1 == "2" and respuesta2 == "2" and respuesta3 == "2" and respuesta4 == "2" and respuesta5 == "2":
    print("Te recomendamos relajarte viendo películas o leyendo en casa.")
else:
    print("Basado en tus respuestas, podrías disfrutar de varias actividades de ocio. ¡Explora y diviértete!")