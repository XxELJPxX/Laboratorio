import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        # Obtener valores
        peso = float(entry_peso.get())
        estatura = float(entry_estatura.get())
        
        # Validar que sean positivos
        if peso <= 0:
            messagebox.showerror("Error", "El peso debe ser un valor positivo")
            return
        
        if estatura <= 0:
            messagebox.showerror("Error", "La estatura debe ser un valor positivo")
            return
        
        # Calcular IMC = Peso / (Estatura)^2
        imc = peso / (estatura ** 2)
        
        # Determinar el estado según el IMC
        if 19 <= imc <= 24:
            mensaje = "¡Excelente! Tienes el peso ideal."
        elif 25 <= imc <= 29:
            mensaje = "¡Cuidado! Tienes sobrepeso."
        elif imc >= 30:
            mensaje = "¡Urgente! Tienes obesidad."
        else:
            mensaje = "IMC por debajo del rango."
        
        # Mostrar resultado
        label_resultado.config(text=f"IMC = {imc:.2f}\n{mensaje}")
        
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos")

def limpiar():
    entry_peso.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    label_resultado.config(text="")

# Crear ventana
ventana = tk.Tk()
ventana.title("Control de Peso Saludable")
ventana.geometry("400x350")

# Título
tk.Label(ventana, text="Control de Peso Saludable", font=("Arial", 14, "bold")).pack(pady=10)

# Fórmula
tk.Label(ventana, text="IMC = Peso / (Estatura)²", font=("Arial", 10)).pack(pady=5)

# Campos de entrada
frame = tk.Frame(ventana)
frame.pack(pady=20)

tk.Label(frame, text="Peso (kg):").grid(row=0, column=0, padx=5, pady=10, sticky="e")
entry_peso = tk.Entry(frame, width=15)
entry_peso.grid(row=0, column=1, padx=5, pady=10)

tk.Label(frame, text="Estatura (m):").grid(row=1, column=0, padx=5, pady=10, sticky="e")
entry_estatura = tk.Entry(frame, width=15)
entry_estatura.grid(row=1, column=1, padx=5, pady=10)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Calcular", command=calcular_imc, width=10).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Limpiar", command=limpiar, width=10).grid(row=0, column=1, padx=5)

# Resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"), fg="blue")
label_resultado.pack(pady=20)

# Información de rangos
tk.Label(ventana, text="Rangos:", font=("Arial", 9, "bold")).pack()
tk.Label(ventana, text="19-24: Peso ideal | 25-29: Sobrepeso | 30+: Obesidad", font=("Arial", 8)).pack()

ventana.mainloop()