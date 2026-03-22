# ==============================
# IMPORTACIÓN
# ==============================

# Importamos tkinter con alias "tk"
# Esto nos permite escribir menos código (tk.Button en vez de tkinter.Button)
import tkinter as tk

# Importamos messagebox para mostrar ventanas emergentes (alertas)
from tkinter import messagebox


# ==============================
# CREACIÓN DE LA VENTANA PRINCIPAL
# ==============================

# Tk() crea la ventana principal de la aplicación
ventana = tk.Tk()

# title() define el nombre de la ventana
ventana.title("Mi App Completa con Tkinter-practica 1")

# geometry() define el tamaño de la ventana (ancho x alto)
ventana.geometry("600x400")

# config() permite cambiar propiedades como color de fondo
ventana.config(bg="#1e1e1e")  # color oscuro


# ==============================
# FUNCIONES (LÓGICA DEL PROGRAMA)
# ==============================

# Esta función se ejecuta cuando el usuario hace clic en el botón
def saludar():
    # get() obtiene el texto que el usuario escribió en el Entry
    nombre = entrada_nombre.get()

    # Validación: si está vacío
    if nombre == "":
        messagebox.showwarning("Advertencia", "Por favor escribe tu nombre")
    else:
        # Mostrar mensaje en pantalla (Label)
        resultado.config(text=f"Hola {nombre} 👋", fg="white")

        # También mostrar ventana emergente
        messagebox.showinfo("Saludo", f"Hola {nombre}, bienvenido 😎")


# Función para limpiar el campo de texto
def limpiar():
    # delete(0, END) borra desde el inicio hasta el final
    entrada_nombre.delete(0, tk.END)
    resultado.config(text="")  # limpiar resultado


# Función para cerrar la app
def salir():
    ventana.quit()


# ==============================
# WIDGETS (ELEMENTOS DE LA INTERFAZ)
# ==============================

# Label = texto en pantalla
titulo = tk.Label(
    ventana,
    text="Bienvenido a la App",
    font=("Arial", 20),   # tipo y tamaño de letra
    bg="#1e1e1e",         # fondo
    fg="white"            # color del texto
)

# pack() coloca el elemento en la ventana
# pady agrega espacio vertical
titulo.pack(pady=20)


# Label para indicar qué hacer
label_nombre = tk.Label(
    ventana,
    text="Escribe tu nombre:",
    bg="#1e1e1e",
    fg="white"
)
label_nombre.pack()


# Entry = campo de texto
entrada_nombre = tk.Entry(
    ventana,
    width=30  # ancho del campo
)
entrada_nombre.pack(pady=5)


# Button = botón
boton_saludar = tk.Button(
    ventana,
    text="Saludar",
    command=saludar,   # función que se ejecuta al hacer clic
    bg="#4CAF50",      # color de fondo
    fg="white"
)
boton_saludar.pack(pady=5)


# Botón limpiar
boton_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    command=limpiar,
    bg="#f39c12",
    fg="white"
)
boton_limpiar.pack(pady=5)


# Botón salir
boton_salir = tk.Button(
    ventana,
    text="Salir",
    command=salir,
    bg="#e74c3c",
    fg="white"
)
boton_salir.pack(pady=5)


# Label para mostrar resultado dinámico
resultado = tk.Label(
    ventana,
    text="",
    font=("Arial", 14),
    bg="#1e1e1e"
)
resultado.pack(pady=20)


# ==============================
# RESUMEN CÓDIGO
# ==============================

# - Tk() → ventana principal
# - Label → mostrar texto
# - Entry → entrada de usuario
# - Button → botones interactivos
# - command → conecta botón con función
# - pack() → organiza elementos (hay otros como grid() y place())
# - get() → obtener texto
# - delete() → borrar texto
# - config() → cambiar propiedades dinámicamente
# - messagebox → ventanas emergentes
# - funciones → lógica de la app


# ==============================
# BUCLE PRINCIPAL
# ==============================

# mainloop() mantiene la ventana abierta
# Sin esto, la app se cierra inmediatamente
ventana.mainloop()