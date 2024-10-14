# accounts.py
class Accounts:
    def __init__(self):
        self.accounts_receivable = []
        self.accounts_payable = []

    def add_receivable(self, client, amount, due_date):
        """Añade una cuenta por cobrar."""
        self.accounts_receivable.append({'client': client, 'amount': amount, 'due_date': due_date})

    def add_payable(self, supplier, amount, due_date):
        """Añade una cuenta por pagar."""
        self.accounts_payable.append({'supplier': supplier, 'amount': amount, 'due_date': due_date})

    def get_outstanding_receivables(self):
        """Obtiene las cuentas por cobrar pendientes."""
        return [rec for rec in self.accounts_receivable if rec['due_date'] >= '2024-10-13']

    def get_outstanding_payables(self):
        """Obtiene las cuentas por pagar pendientes."""
        return [pay for pay in self.accounts_payable if pay['due_date'] >= '2024-10-13']
