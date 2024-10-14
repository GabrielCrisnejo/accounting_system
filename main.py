# main.py
from src.inventory import Inventory
from src.billing import Billing
from src.accounts import Accounts
from src.financial import Financial
from src.security import Security
from src.reporting import Reporting

# Inicialización de los módulos
inventory = Inventory()
billing = Billing()
accounts = Accounts()
financial = Financial()
security = Security()
reporting = Reporting()

# Ejemplo de flujo de trabajo
inventory.add_product('A001', 'Filtro de Aceite', 'Filtros', 50, 15)
inventory.add_product('A002', 'Bujía', 'Encendido', 30, 10)

print(inventory.get_stock())

billing.create_sale_invoice('Cliente 1', [{'price': 15, 'quantity': 2}, {'price': 10, 'quantity': 4}])

print(billing.get_invoices())

accounts.add_receivable('Cliente 1', 70, '2024-11-01')

print(accounts.get_outstanding_receivables())

financial.record_entry('Venta de repuestos', 70, 0)

print(financial.balance_sheet())

security.add_user('admin', 'admin123', 'admin')
print(security.authenticate('admin', 'admin123'))

print(reporting.generate_sales_report(billing.sales_invoices))
