import tkinter as tk
 
def verificar_primo():
    try:
        n = int(entrada_numero.get())
        if n < 2:
            resultado.config(text="No es un número primo")
            return
 
        es_primo = True
        con = 2
 
        while con <= n - 1:
            if n % con == 0:
                es_primo = False
                break
            con += 1
 
        if es_primo:
            resultado.config(text=f"{n} es un número primo")
        else:
            resultado.config(text=f"{n} no es un número primo")
 
    except ValueError:
        resultado.config(text="Por favor, ingrese un número válido")
 
# Ventana principal
ventana = tk.Tk()
ventana.title("Verificar si un número es primo")
ventana.configure(bg="#7fbadb")
ventana.geometry("500x200")
 
 
tk.Label(ventana, text="Ingrese un número:", bg="#7fbadb").pack(pady=5)
entrada_numero = tk.Entry(ventana)
entrada_numero.pack(pady=5)
 
tk.Button(ventana, text="Verificar", command=verificar_primo).pack(pady=5)
 
resultado = tk.Label(ventana, text="", bg="#d9d9d9")
resultado.pack(pady=10)
 
ventana.mainloop()
 
 