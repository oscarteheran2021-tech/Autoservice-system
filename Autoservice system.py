import tkinter as tk
from tkinter import messagebox

# --- TUS DATOS Y BACKEND ORIGINAL (INTACTOS) ---
productos = [
    {"nombre": "Salchipapa", "precio": "10.000 COP", "stock": 10},
    {"nombre": "Arepa", "precio": "5.000 COP", "stock": 20},
    {"nombre": "Hamburguesa", "precio": "15.000 COP", "stock": 5},
]

total_facturado = 0


# --- CONFIGURACIÓN DE LA INTERFAZ GRÁFICA (GUI) ---
root = tk.Tk()
root.title("Sistema de Tienda - Compras")
root.geometry("450x550")
root.config(bg="#f0f0f0")

# Título principal
titulo = tk.Label(root, text="Bienvenido al Sistema de Tienda",
                  font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333")
titulo.pack(pady=10)

# Mostrar inventario inicial en pantalla
frame_inventario = tk.LabelFrame(
    root, text=" Productos Disponibles ", font=("Arial", 10, "bold"), bg="#f0f0f0")
frame_inventario.pack(fill="x", padx=20, pady=5)

for i in productos:
    lbl_prod = tk.Label(frame_inventario, text=f"• {i['nombre']} = {i['precio']}  (Stock: {i['stock']})", font=(
        "Arial", 10), bg="#f0f0f0", anchor="w")
    lbl_prod.pack(fill="x", padx=10, anchor="w")

# Sección de entradas (Inputs)
frame_entradas = tk.Frame(root, bg="#f0f0f0")
frame_entradas.pack(pady=10)

lbl_nombre = tk.Label(frame_entradas, text="¿Qué producto deseas comprar?:", font=(
    "Arial", 10), bg="#f0f0f0")
lbl_nombre.grid(row=0, column=0, sticky="w", pady=5)
entry_nombre = tk.Entry(frame_entradas, font=("Arial", 10), width=20)
entry_nombre.grid(row=0, column=1, pady=5, padx=5)

lbl_cantidad = tk.Label(frame_entradas, text="¿Cuántas unidades deseas?:", font=(
    "Arial", 10), bg="#f0f0f0")
lbl_cantidad.grid(row=1, column=0, sticky="w", pady=5)
entry_cantidad = tk.Entry(frame_entradas, font=("Arial", 10), width=20)
entry_cantidad.grid(row=1, column=1, pady=5, padx=5)

# Consola de texto para mostrar los mensajes del sistema
frame_consola = tk.Frame(root)
frame_consola.pack(fill="both", expand=True, padx=20, pady=5)

txt_consola = tk.Text(frame_consola, height=8, font=(
    "Consolas", 9), bg="#1e1e1e", fg="#00ff00")
txt_consola.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_consola, command=txt_consola.yview)
scrollbar.pack(side="right", fill="y")
txt_consola.config(yscrollcommand=scrollbar.set)

# Mensaje inicial en la consola
txt_consola.insert(tk.END, "=== Sistema iniciado correctamente ===\n")


# --- FUNCIÓN QUE CONECTA LOS BOTONES CON TU LÓGICA ---
def procesar_compra():
    global total_facturado
    nombre_producto = entry_nombre.get().strip()
    cantidad_str = entry_cantidad.get().strip()

    # Validar que la cantidad sea un número
    if not cantidad_str.isdigit():
        messagebox.showerror(
            "Error", "Por favor ingresa un número válido para la cantidad.")
        return

    cantidad = int(cantidad_str)

    # --- AQUÍ ESTÁ EXACTAMENTE TU BÚSQUEDA DEL BACKEND ---
    producto_encontrado = False

    for producto in productos:
        if producto["nombre"].lower() == nombre_producto.lower():
            producto_encontrado = True

            if cantidad <= producto["stock"]:
                total = cantidad * \
                    int(producto["precio"].split()[0].replace(".", ""))
                total_facturado += total
                producto["stock"] -= cantidad

                # Imprimir en la consola gráfica
                txt_consola.insert(
                    tk.END, f"¡Éxito! Añadiste a tu compra {cantidad} {producto['nombre']} por {total:,} COP\n")
            else:
                txt_consola.insert(
                    tk.END, f"❌ No hay stock de {producto['nombre']}. Disponible: {producto['stock']}\n")

            break

    if not producto_encontrado:
        txt_consola.insert(
            tk.END, f"❌ Producto '{nombre_producto}' no encontrado.\n")

    # Limpiar los inputs para la siguiente compra
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    txt_consola.see(tk.END)


def finalizar_programa():
    # --- AQUÍ ESTÁ EXACTAMENTE TU BLOQUE FINAL ---
    txt_consola.insert(tk.END, "\n" + "="*35 + "\n")
    txt_consola.insert(
        tk.END, f" Gracias por su compra. Total facturado: {total_facturado:,} COP\n")
    txt_consola.insert(tk.END, "="*35 + "\n")

    # Deshabilitar botones al terminar
    btn_comprar.config(state="disabled")
    btn_terminar.config(state="disabled")
    messagebox.showinfo(
        "Ticket Final", f"Gracias por su compra.\nEl total facturado es: {total_facturado:,} COP")


# Botones de acción interfaz
frame_botones = tk.Frame(root, bg="#f0f0f0")
frame_botones.pack(pady=10)

btn_comprar = tk.Button(frame_botones, text="Añadir a la Compra", font=(
    "Arial", 10, "bold"), bg="#4CAF50", fg="white", command=procesar_compra)
btn_comprar.pack(side="left", padx=5)

btn_terminar = tk.Button(frame_botones, text="Terminar y Pagar", font=(
    "Arial", 10, "bold"), bg="#f44336", fg="white", command=finalizar_programa)
btn_terminar.pack(side="left", padx=5)

# Ejecutar la ventana
root.mainloop()
