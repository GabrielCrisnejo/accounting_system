# financial.py
class Financial:
    def __init__(self):
        self.entries = []

    def record_entry(self, description, debit, credit):
        """Registra una entrada en el libro mayor."""
        self.entries.append({
            'description': description,
            'debit': debit,
            'credit': credit
        })

    def balance_sheet(self):
        """Genera el balance general."""
        total_debit = sum(entry['debit'] for entry in self.entries)
        total_credit = sum(entry['credit'] for entry in self.entries)
        return {
            'Total Debit': total_debit,
            'Total Credit': total_credit,
            'Balance': total_debit - total_credit
        }

    def income_statement(self):
        """Genera el estado de resultados."""
        return {
            'Total Income': sum(entry['debit'] for entry in self.entries),
            'Total Expenses': sum(entry['credit'] for entry in self.entries)
        }