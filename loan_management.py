class loan:
    def __init__(self,loan_type,amount,account_id,interest_rate,term):
        self.loan = loan 
        self.type = type 
        self.amount = amount 
        self.account_id = account_id
        self.interest_rate = interest_rate
        self.term = term 
        self.status = "active "
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






