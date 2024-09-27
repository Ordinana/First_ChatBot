import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Necesitarás instalar Pillow: pip install Pillow
import os

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Chatbot de BAÏA")
ventana.geometry("500x600")
ventana.configure(bg='white')

# Habilitar el redimensionamiento
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)

# Lista global para mantener referencias a las burbujas
lista_burbujas = []

# Marco superior para el avatar y el nombre del chatbot
top_frame = tk.Frame(ventana, bg='white')
top_frame.grid(row=0, column=0, sticky='ew')

# Permitir que el top_frame se expanda horizontalmente
top_frame.columnconfigure(1, weight=1)

# Cargar la imagen del avatar
try:
    ruta_imagen = os.path.join(os.path.dirname(__file__), 'avatar.png')
    avatar_image = Image.open(ruta_imagen)
    avatar_image = avatar_image.resize((50, 50), Image.LANCZOS)
    avatar_photo = ImageTk.PhotoImage(avatar_image)
except Exception as e:
    print(f"Error al cargar la imagen del avatar desde {ruta_imagen}: {e}")
    avatar_photo = None

# Etiqueta del avatar
if avatar_photo:
    avatar_label = tk.Label(top_frame, image=avatar_photo, bg='white')
    avatar_label.image = avatar_photo  # Mantener una referencia
    avatar_label.grid(row=0, column=0, padx=10, pady=5)
else:
    # Si no se carga la imagen, mostrar un texto como reemplazo
    avatar_label = tk.Label(top_frame, text="[Avatar]", bg='white', font=("Helvetica", 12))
    avatar_label.grid(row=0, column=0, padx=10, pady=5)

# Etiqueta con el nombre del chatbot
chatbot_name_label = tk.Label(top_frame, text="Chatbot de BAÏA", bg='white', font=("Helvetica", 16, "bold"))
chatbot_name_label.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# Marco para los mensajes del chat
chat_frame = tk.Frame(ventana, bg='white')
chat_frame.grid(row=1, column=0, sticky='nsew')

# Canvas y scrollbar para los mensajes
canvas = tk.Canvas(chat_frame, bg='white', highlightthickness=0)
scrollbar = ttk.Scrollbar(chat_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg='white')

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Marco para las opciones
options_frame = tk.Frame(ventana, bg='white')
options_frame.grid(row=2, column=0, sticky='ew')

# Variables globales
respuestas = []
indice_pregunta = -1  # Iniciamos en -1 para pedir el nombre
nombre = ""
tiempo_espera = 500  # Tiempo de espera predeterminado en milisegundos

# Definición de las preguntas y opciones
preguntas = [
    {
        "texto": "¿Crees que este chatbot te va a solucionar la vida, o es solo otra excusa para perder el tiempo?",
        "opciones": [
            "Sí",
            "No, es una excusa perfecta para seguir procrastinando"
        ]
    },
    {
        "texto": "¿Has probado buscar en Google '¿cómo no perder el tiempo'?",
        "opciones": [
            "¡Sí!",
            "No..."
        ]
    },
    {
        "texto": "¿Le has preguntado a tu madre? Las madres siempre tienen la respuesta",
        "opciones": [
            "Sí, pero dice que la culpa es de TikTok",
            "No, quiero seguir buscándolo por mi cuenta"
        ]
    },
    {
        "texto": "¿Le has mandado ya el trabajo final a tu profe?",
        "opciones": [
            "Sí",
            "No, aún queda un día, ya lo haré mañana"
        ]
    },
    {
        "texto": "¿Entonces, crees que con BAÏA podrás dejar de procrastinar de una vez?",
        "opciones": [
            "Sí, supongo.",
            "¿Por qué iba a creerlo?"
        ]
    }
]

# Función para agregar mensajes del chatbot al chat
def agregar_mensaje_chatbot(mensaje, bold=True, border_color=None, bg_color='#F0F0F0'):
    # Crear un marco para el mensaje
    message_frame = tk.Frame(scrollable_frame, bg='white')
    message_frame.pack(anchor='w', padx=10, pady=5, fill='x')

    # Definir la fuente según el parámetro bold
    if bold:
        font_style = ("Helvetica", 13, "bold")
    else:
        font_style = ("Helvetica", 13)

    # Crear la burbuja de mensaje
    bubble = tk.Label(
        message_frame,
        text=mensaje,
        bg=bg_color,
        fg='black',
        justify='left',
        font=font_style,
        bd=0,
        padx=10,
        pady=5,
        wraplength=ventana.winfo_width() - 100
    )

    # Si se especifica un color de borde, aplicarlo
    if border_color:
        bubble.config(highlightbackground=border_color, highlightcolor=border_color, highlightthickness=1)

    bubble.pack(anchor='w', fill='x')

    # Agregar la burbuja a la lista global
    lista_burbujas.append(bubble)

    # Actualizar el canvas
    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

# Función para agregar mensajes del usuario al chat
def agregar_mensaje_usuario(mensaje):
    # Crear un marco para el mensaje
    message_frame = tk.Frame(scrollable_frame, bg='white')
    message_frame.pack(anchor='e', padx=10, pady=5, fill='x')

    # Crear la burbuja de mensaje
    bubble = tk.Label(
        message_frame,
        text=mensaje,
        bg='white',
        fg='black',
        justify='left',
        font=("Helvetica", 13, "bold"),
        bd=1,
        relief="solid",
        padx=10,
        pady=5,
        wraplength=ventana.winfo_width() - 100
    )
    bubble.config(highlightbackground='#FFA500', highlightcolor='#FFA500', highlightthickness=1)
    bubble.pack(anchor='e', fill='x')

    # Agregar la burbuja a la lista global
    lista_burbujas.append(bubble)

    # Actualizar el canvas
    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

# Función para mostrar las opciones como botones estilo burbuja con borde naranja
def mostrar_opciones(opciones):
    # Limpiar opciones anteriores
    for widget in options_frame.winfo_children():
        widget.destroy()

    for idx, opcion_texto in enumerate(opciones):
        # Crear un marco para la opción con borde naranja
        opcion_frame = tk.Frame(options_frame, bg='white', highlightbackground='#FFA500',
                                highlightcolor='#FFA500', highlightthickness=1)
        opcion_frame.pack(anchor='w', padx=10, pady=5, fill='x')

        opcion_button = tk.Button(
            opcion_frame,
            text=opcion_texto,
            command=lambda idx=idx: seleccionar_opcion(idx + 1),
            wraplength=ventana.winfo_width() - 60,
            justify='left',
            font=("Helvetica", 13),
            bd=0,
            padx=10,
            pady=5,
            bg='#E0E0E0',
            fg='black',
            activebackground='#D5D5D5'
        )
        opcion_button.pack(fill='x')

# Función para manejar la selección de una opción
def seleccionar_opcion(opcion_index):
    global indice_pregunta, nombre, tiempo_espera
    if indice_pregunta == -1:
        # No se espera seleccionar una opción aquí
        pass
    else:
        respuestas.append(str(opcion_index))
        opcion_texto = preguntas[indice_pregunta]['opciones'][opcion_index - 1]
        agregar_mensaje_usuario(opcion_texto)
        tiempo_extra = manejar_respuesta(opcion_index)
        indice_pregunta += 1
        for widget in options_frame.winfo_children():
            widget.destroy()
        if indice_pregunta < len(preguntas):
            ventana.after(tiempo_espera + tiempo_extra, mostrar_pregunta)
        else:
            ventana.after(tiempo_espera + tiempo_extra, mostrar_procesando)

# Función para manejar respuestas específicas
def manejar_respuesta(opcion):
    mensajes_especiales = {
        0: {1: "Mentiros@", 2: ""},
        1: {1: "Mentiros@", 2: "Pues búscalo vag@"},
        3: {1: "Mentiros@", 2: "¿A qué esperas?"}
    }
    tiempo_extra = 0
    if indice_pregunta in mensajes_especiales and opcion in mensajes_especiales[indice_pregunta]:
        mensaje = mensajes_especiales[indice_pregunta][opcion]
        if mensaje:
            agregar_mensaje_chatbot(mensaje, bold=False)  # Texto sin negrita
            tiempo_extra = 500  # Tiempo adicional de espera en milisegundos
    return tiempo_extra

# Función para mostrar la pregunta actual
def mostrar_pregunta():
    global indice_pregunta
    if indice_pregunta == -1:
        agregar_mensaje_chatbot("¿Cuál es tu nombre?")
        mostrar_campo_nombre()
    elif indice_pregunta < len(preguntas):
        agregar_mensaje_chatbot(preguntas[indice_pregunta]['texto'])
        mostrar_opciones(preguntas[indice_pregunta]['opciones'])
    else:
        mostrar_procesando()

# Función para mostrar el campo para ingresar el nombre
def mostrar_campo_nombre():
    # Limpiar opciones anteriores
    for widget in options_frame.winfo_children():
        widget.destroy()

    global nombre_entry
    nombre_entry = tk.Entry(options_frame, font=("Helvetica", 13))
    nombre_entry.pack(padx=10, pady=5, fill='x')
    nombre_entry.bind("<Return>", enviar_nombre)

    enviar_button = tk.Button(
        options_frame,
        text="Enviar",
        command=enviar_nombre,
        font=("Helvetica", 13),
        bg='#E0E0E0',
        fg='black',
        bd=0,
        activebackground='#D5D5D5'
    )
    enviar_button.pack(padx=10, pady=5)

# Función para enviar el nombre
def enviar_nombre(event=None):
    global nombre, indice_pregunta
    nombre = nombre_entry.get().strip()
    if nombre:
        agregar_mensaje_usuario(nombre)
        agregar_mensaje_chatbot(f"¡¡Hola {nombre}!! Empecemos...")
        indice_pregunta = 0
        for widget in options_frame.winfo_children():
            widget.destroy()
        ventana.after(500, mostrar_pregunta)
    else:
        agregar_mensaje_chatbot("Por favor, ingresa tu nombre.")

# Función para mostrar "Procesando recomendación..."
def mostrar_procesando():
    agregar_mensaje_chatbot("Procesando recomendación...")
    ventana.after(1000, generar_recomendacion)

# Función para generar y mostrar la recomendación final
def generar_recomendacion():
    if (respuestas == ["1", "1", "1", "1", "1"]):
        recomendacion = "Estupendo, nuestra solución BAÏA te ayudará mucho."
    elif (respuestas == ["1", "2", "1", "1", "1"]):
        recomendacion = "No seas pesado y cómprala ya."
    elif (respuestas == ["2", "1", "2", "1", "2"]):
        recomendacion = "Consulta a un profesional, tu procrastinación no tiene solución."
    elif (respuestas == ["2", "2", "2", "2", "2"]):
        recomendacion = "Deja de perder el tiempo y actúa."
    else:
        recomendacion = "Necesitas cambiar de estrategia para combatir la procrastinación."
    # Mostrar la recomendación con fondo naranja y borde negro
    agregar_mensaje_chatbot(
        f"{nombre}, {recomendacion}",
        border_color='black',
        bg_color='#FFA500'
    )
    # Desactivar el marco de opciones
    for widget in options_frame.winfo_children():
        widget.destroy()

# Función para actualizar el wraplength de las burbujas al redimensionar
def actualizar_wraplength(event=None):
    new_width = ventana.winfo_width() - 100  # Ajusta este valor según tus necesidades
    for bubble in lista_burbujas:
        bubble.config(wraplength=new_width)

    # Actualizar wraplength de los botones de opciones
    for widget in options_frame.winfo_children():
        if isinstance(widget, tk.Frame):
            for child in widget.winfo_children():
                if isinstance(child, tk.Button):
                    child.config(wraplength=new_width - 20)

ventana.bind('<Configure>', actualizar_wraplength)

# Función para iniciar la conversación
def iniciar_conversacion():
    agregar_mensaje_chatbot("¡Hola! Soy el chatbot de BAÏA.")
    ventana.after(10, actualizar_wraplength)  # Actualizar wraplength después de agregar el mensaje inicial
    ventana.after(500, mostrar_pregunta)

# Iniciar la conversación
iniciar_conversacion()

# Iniciar el bucle de la interfaz
ventana.mainloop()
