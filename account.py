class Account:
    def __init__(self, account_id, balance=0, account_type="checking"):
        self.account_id = account_id
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
    
    def get_details(self):
        return {
            "account_id": self.account_id,
            "balance": self.balance,
            "account_type": self.account_type
        }
    