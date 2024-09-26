import time

print("\n¡Hola! Soy el chatbot de BAÏA\n")
nombre = input("Tu nombre porfavor (En verdad nos da igual pero es lo correctamente político): ")
print(f"¡¡Hola {nombre}!! Empecemos...")
time.sleep(1.5)

# Pregunta 1 con validación
while True:
    print("\nPregunta 1: ¿Crees que este chatbot te va a solucionar la vida, o es solo otra excusa para perder el tiempo?")
    print("1. Si")
    print("2. No, es una excusa perfecta para seguir procastinando")
    respuesta1 = input("Selecciona 1 o 2: ")
    if respuesta1 == "1" or respuesta1 == "2":
        if respuesta1 == "1":
            print("Mentiros@")
        else:
            pass
        break  # Entrada válida, salir del bucle
    else:
        print("¡¡Centrate de una vez y por favor, selecciona 1 o 2.")

# Pregunta 2 con validación
while True:
    print("\nPregunta 2: ¿Has probado buscar en google “como no perder el tiempo?")
    print("1. Sí.")
    print("2. No, búscalo vago")
    respuesta2 = input("Selecciona 1 o 2: ")
    if respuesta2 == "1" or respuesta2 == "2":
        if respuesta2 == "1":
            print("Mentiros@")
        else:
            print("Pues búscalo vag@")
        break
    else:
        print("¡¡Entrada no válida!!. Por favor, selecciona 1 o 2.")

# Pregunta 3 con validación
while True:
    print("\nPregunta 3: ¿Le has preguntado a tu madre? Las madres siempre tienen la respuesta")
    print("1. Sí, hazle caso a tu madre")
    print("2. No, quiero seguir buscando el sentido a mi vida")
    respuesta3 = input("Selecciona 1 o 2: ")
    if respuesta3 == "1" or respuesta3 == "2":
        break
    else:
        print("¡¡Entrada no válida!!. Por favor, selecciona 1 o 2.")

# Pregunta 4 con validación
while True:
    print("\nPregunta 4: ¿Le has mandado ya el mail a tu jefe?")
    print("1. Sí")
    print("2. No")
    respuesta4 = input("Selecciona 1 o 2: ")
    if respuesta4 == "1" or respuesta4 == "2":
        if respuesta4 == "1":
            print("Mentiros@")
        else:
            print("¿A que esperas?")
        break
    else:
        print("¡¡Entrada no válida!!. Por favor, selecciona 1 o 2.")

# Pregunta 5 con validación
while True:
    print("\nPregunta 5: ¿Entonces, vas a comprar BAÏA y dejar de procastinar de una vez?")
    print("1. Sí")
    print("2. Sí")
    respuesta5 = input("Selecciona 1 o 2: ")
    if respuesta5 == "1" or respuesta5 == "2":
        break
    else:
        print("¡¡Entrada no válida!!. Por favor, selecciona 1 o 2.")

print("\nProcesando recomendación", end='', flush=True)

for i in range(5):
    time.sleep(0.5)
    print(".", end='', flush=True)

print("\n")

if respuesta1 == "1" and respuesta2 == "1" and respuesta3 == "1" and respuesta4 == "1" and respuesta5 == "1":
    print("Estupendo, nuestra droga BAÏA te ayudará de locos!")
elif respuesta1 == "1" and respuesta2 == "2" and respuesta3 == "1" and respuesta4 == "1" and respuesta5 == "1":
    print("No seas pesado y comprala ya.")
elif respuesta1 == "2" and respuesta2 == "1" and respuesta3 == "2" and respuesta4 == "1" and respuesta5 == "2":
    print("Llama a tu psicólogo, que tu procrastinacion no tiene solución.")
elif respuesta1 == "2" and respuesta2 == "2" and respuesta3 == "2" and respuesta4 == "2" and respuesta5 == "2":
    print("Cállate ya y deja de perder el tiempo, panoli.")
else:
    print("No tienes solución, pilla otra droga")