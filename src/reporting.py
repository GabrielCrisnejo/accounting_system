# reporting.py
class Reporting:
    def generate_sales_report(self, sales_invoices):
        """Genera un reporte de ventas."""
        total_sales = sum(inv['total'] for inv in sales_invoices)
        return {
            'Total Sales': total_sales,
            'Total Invoices': len(sales_invoices)
        }

    def generate_inventory_report(self, inventory):
        """Genera un reporte de inventario."""
        report = {code: product for code, product in inventory.items()}
        return report
