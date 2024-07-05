import tkinter as tk
from tkinter import ttk, messagebox

class BudgetPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Planner")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        self.total_income = 0.0
        self.total_expenses = 0.0

        
        self.title_label = tk.Label(root, text="Budget Planner", font=("Arial", 16), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.income_frame = ttk.LabelFrame(root, text="Add Income", padding=(10, 10))
        self.income_frame.pack(pady=10, padx=10, fill=tk.X)

        self.income_label = ttk.Label(self.income_frame, text="Description:")
        self.income_label.grid(row=0, column=0, padx=5, pady=5)
        self.income_desc_entry = ttk.Entry(self.income_frame, width=20)
        self.income_desc_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = ttk.Label(self.income_frame, text="Amount:")
        self.amount_label.grid(row=0, column=2, padx=5, pady=5)
        self.income_amount_entry = ttk.Entry(self.income_frame, width=10)
        self.income_amount_entry.grid(row=0, column=3, padx=5, pady=5)

        self.add_income_button = ttk.Button(self.income_frame, text="Add Income", style="Cute.TButton", command=self.add_income)
        self.add_income_button.grid(row=0, column=4, padx=5, pady=5)

        self.expense_frame = ttk.LabelFrame(root, text="Add Expense", padding=(10, 10))
        self.expense_frame.pack(pady=10, padx=10, fill=tk.X)

        self.expense_label = ttk.Label(self.expense_frame, text="Description:")
        self.expense_label.grid(row=0, column=0, padx=5, pady=5)
        self.expense_desc_entry = ttk.Entry(self.expense_frame, width=20)
        self.expense_desc_entry.grid(row=0, column=1, padx=5, pady=5)

        self.expense_amount_label = ttk.Label(self.expense_frame, text="Amount:")
        self.expense_amount_label.grid(row=0, column=2, padx=5, pady=5)
        self.expense_amount_entry = ttk.Entry(self.expense_frame, width=10)
        self.expense_amount_entry.grid(row=0, column=3, padx=5, pady=5)

        self.add_expense_button = ttk.Button(self.expense_frame, text="Add Expense", style="Cute.TButton", command=self.add_expense)
        self.add_expense_button.grid(row=0, column=4, padx=5, pady=5)

        self.balance_frame = ttk.LabelFrame(root, text="Balance", padding=(10, 10))
        self.balance_frame.pack(pady=10, padx=10, fill=tk.X)

        self.balance_label = ttk.Label(self.balance_frame, text="Total Balance: $0.00", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        self.style = ttk.Style()
        self.style.configure("Cute.TButton", foreground="#ffffff", background="#3498db", font=("Arial", 10, "bold"))
        self.style.map("Cute.TButton", foreground=[("active", "#ffffff"), ("disabled", "#aaaaaa")],
                       background=[("active", "#2980b9"), ("disabled", "#dddddd")])

    def add_income(self):
        try:
            amount = float(self.income_amount_entry.get())
            self.total_income += amount
            self.update_balance()
            self.income_desc_entry.delete(0, tk.END)
            self.income_amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid amount for income.")

    def add_expense(self):
        try:
            amount = float(self.expense_amount_entry.get())
            self.total_expenses += amount
            self.update_balance()
            self.expense_desc_entry.delete(0, tk.END)
            self.expense_amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid amount for expense.")

    def update_balance(self):
        total_balance = self.total_income - self.total_expenses
        self.balance_label.config(text=f"Total Balance: ${total_balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetPlanner(root)
    root.mainloop()
