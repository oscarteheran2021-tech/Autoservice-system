# 🛒 Store Inventory and Billing System (Python + Tkinter)

Desktop application developed in Python that implements a complete inventory management and billing system. The project evolves from a console-based logic using dictionaries and lists to an interactive graphical user interface built with **Tkinter**.

---

## ⚙️ How the Code Works (Structure and Logic)

The source code is structured modularly to separate data, business logic, and the user interface:

### 1. Data Structure (Backend)
- **Dictionaries and Lists:** The inventory is stored in a list of dictionaries, where each product contains specific keys (`"nombre"`, `"precio"`, and `"stock"`):
  ```python
  productos = [
      {"nombre": "Salchipapa", "precio": "10.000 COP", "stock": 10},
      {"nombre": "Arepa", "precio": "5.000 COP", "stock": 20},
      {"nombre": "Hamburguesa", "precio": "15.000 COP", "stock": 5},
  ]
