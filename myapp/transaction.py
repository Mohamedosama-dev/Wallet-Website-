from datetime import datetime

class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
