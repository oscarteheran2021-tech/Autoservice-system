# 🛒 Sistema de Tienda y Facturación (Python + Tkinter)

Aplicación de escritorio desarrollada en Python que implementa un sistema completo de gestión de inventario y facturación. El proyecto evoluciona desde una lógica de consola basada en diccionarios y listas hasta una interfaz gráfica interactiva construida con **Tkinter**.

---

## ⚙️ ¿Cómo Funciona el Código? (Estructura y Lógica)

El código fuente está estructurado de manera modular para separar los datos, la lógica de negocio y la interfaz de usuario:

### 1. Estructura de Datos (Backend)
* **Diccionarios y Listas:** El inventario se almacena en una lista de diccionarios, donde cada producto contiene claves específicas (`"nombre"`, `"precio"` y `"stock"`):
  ```python
  productos = [
      {"nombre": "Salchipapa", "precio": "10.000 COP", "stock": 10},
      {"nombre": "Arepa", "precio": "5.000 COP", "stock": 20},
      {"nombre": "Hamburguesa", "precio": "15.000 COP", "stock": 5},
  ]
