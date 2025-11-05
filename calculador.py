#Juan Pablo Martin Carrion y Kevin Diaz
#05/11/2025
#Funcion calculador de expresion matematica con TK
import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        # Obtener valores
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        # Validar restricciones
        if b == 0:
            messagebox.showerror("Error", "b no puede ser cero")
            return
        
        if c == 0:
            messagebox.showerror("Error", "c no puede ser cero")
            return
        
        if a == b:
            messagebox.showerror("Error", "a y b deben ser diferentes")
            return
        
        # Calcular x = (-b + 5a + 2c) / (2bc - c)
        numerador = -b + 5*a + 2*c
        denominador = 2*b*c - c
        
        if denominador == 0:
            messagebox.showerror("Error", "El denominador es cero")
            return
        
        x = numerador / denominador
        
        # Mostrar resultado
        label_resultado.config(text=f"x = {x}")
        
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos")

def limpiar():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    label_resultado.config(text="")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Expresión")
ventana.geometry("400x300")

# Título
tk.Label(ventana, text="x = (-b + 5a + 2c) / (2bc - c)", font=("Arial", 12, "bold")).pack(pady=10)

# Restricciones
tk.Label(ventana, text="Restricciones: b ≠ 0, c ≠ 0, a ≠ b", fg="red").pack()

# Campos de entrada
frame = tk.Frame(ventana)
frame.pack(pady=20)

tk.Label(frame, text="a:").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame, width=15)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="b:").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(frame, width=15)
entry_b.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="c:").grid(row=2, column=0, padx=5, pady=5)
entry_c = tk.Entry(frame, width=15)
entry_c.grid(row=2, column=1, padx=5, pady=5)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Calcular", command=calcular, width=10).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Limpiar", command=limpiar, width=10).grid(row=0, column=1, padx=5)

# Resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 14, "bold"), fg="blue")
label_resultado.pack(pady=20)

ventana.mainloop()