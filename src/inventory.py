# inventory.py
class Inventory:
    def __init__(self):
        # Diccionario para almacenar productos y sus atributos
        self.products = {}

    def add_product(self, code, name, category, stock, price):
        """Agrega un producto al inventario."""
        self.products[code] = {
            'name': name,
            'category': category,
            'stock': stock,
            'price': price
        }

    def update_stock(self, code, quantity):
        """Actualiza el stock de un producto."""
        if code in self.products:
            self.products[code]['stock'] += quantity
        else:
            print("Producto no encontrado")

    def get_stock(self):
        """Retorna el inventario completo."""
        return self.products

    def low_stock_alert(self, threshold=5):
        """Alerta de productos con bajo stock."""
        low_stock = {code: p for code, p in self.products.items() if p['stock'] < threshold}
        return low_stock