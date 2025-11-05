import tkinter as tk
 
def calcular_costo():
    hojas = entrada_hojas.get()
 
    try:
        hojas = int(hojas)
        if hojas == 250:
            resultado.config(text="El costo del cuaderno es: $16,000")
        elif hojas == 100:
            resultado.config(text="El costo del cuaderno es: $11,000")
        elif hojas == 80:
            resultado.config(text="El costo del cuaderno es: $8,000")
        elif hojas == 50:
            resultado.config(text="El costo del cuaderno es: $4,500")
        else:
            resultado.config(text="Número de hojas incorrecto.")
    except ValueError:
        resultado.config(text="Por favor, ingrese un número válido.")
 
# Ventana principal
ventana = tk.Tk()
ventana.title("Costo de Cuadernos")
ventana.geometry("500x200")
ventana.configure(bg="#7fbadb")
 
 
tk.Label(ventana, text="Ingrese el número de hojas del cuaderno:").pack(pady=10)
entrada_hojas = tk.Entry(ventana)
entrada_hojas.pack(pady=5)
 
tk.Button(ventana, text="Calcular costo", command=calcular_costo).pack(pady=10)
 
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)
ventana.mainloop()