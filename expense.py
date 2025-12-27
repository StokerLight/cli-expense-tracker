from datetime import datetime

class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = float(amount)
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }