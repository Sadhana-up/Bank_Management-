class Loan:
    def __init__(self, loan_id, account_id, loan_type, amount, interest_rate, term_years):
        self.loan_id = loan_id
        self.account_id = account_id
        self.loan_type = loan_type
        self.amount = amount
        self.interest_rate = interest_rate  
        self.term_years = term_years
        self.balance_remaining = amount
        self.status = "active"
        self.payments = []

    def calculate_total_payable(self):
        total = self.amount * (1 + self.interest_rate * self.term_years)
        return round(total, 2)

    def calculate_monthly_payment(self):
        total = self.calculate_total_payable()
        months = self.term_years * 12
        return round(total / months, 2)

    def make_payment(self, amount):
        if self.status != "active":
            raise ValueError("Loan is not active.")
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")
        self.balance_remaining -= amount
        self.payments.append(amount)

        if self.balance_remaining <= 0:
            self.balance_remaining = 0
            self.status = "paid"

    def get_payment_history(self):
        return self.payments

    def get_remaining_balance(self):
        return round(self.balance_remaining, 2)

    def get_loan_summary(self):
        return {
            "loan_id": self.loan_id,
            "account_id": self.account_id,
            "loan_type": self.loan_type,
            "amount": self.amount,
            "interest_rate": self.interest_rate,
            "term_years": self.term_years,
            "balance_remaining": self.balance_remaining,
            "status": self.status,
            "total_payments_made": sum(self.payments)
        }
