class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.categories = {}

    def add_expense(self, date, amount, category):
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append((date, amount))

#test the function
tracker = ExpenseTracker()
tracker.add_expense("2025-08-31", 200, "Food")
tracker.add_expense("2025-08-30", 100, "Food")
tracker.add_expense("2025-08-29", 500, "Transport")

print(f"{tracker.expenses}")
