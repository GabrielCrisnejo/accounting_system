# billing.py
class Billing:
    def __init__(self):
        self.sales_invoices = []
        self.purchase_invoices = []

    def create_sale_invoice(self, client, products):
        """Crea una factura de venta."""
        invoice = {
            'client': client,
            'products': products,
            'total': sum(item['price'] * item['quantity'] for item in products)
        }
        self.sales_invoices.append(invoice)
        return invoice

    def create_purchase_invoice(self, supplier, products):
        """Crea una factura de compra."""
        invoice = {
            'supplier': supplier,
            'products': products,
            'total': sum(item['price'] * item['quantity'] for item in products)
        }
        self.purchase_invoices.append(invoice)
        return invoice

    def get_invoices(self):
        """Devuelve todas las facturas."""
        return {
            'sales': self.sales_invoices,
            'purchases': self.purchase_invoices
        }
