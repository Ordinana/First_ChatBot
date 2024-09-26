print("¡Hola! Te ayudaré a elegir una bebida.")

print("\nPregunta: ¿Te apetece una bebida caliente o fría?")
print("1. Caliente")
print("2. Fría")
respuesta = input("Selecciona 1 o 2: ")

if respuesta == "1":
    print("\nRecomendación: Podrías tomar un café o un té caliente.")
elif respuesta == "2":
    print("\nRecomendación: ¿Qué tal un jugo frío o una limonada?")
else:
    print("\nEntrada no válida. Por favor, reinicia el programa e intenta de nuevo.")