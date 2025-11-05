class Bank:
    def __init__(self,bank_num,branch,total_balance,transactions,customers,address):

        self.bank_num = bank_num
        self.branch = branch
        self.total_balance = total_balance
        self.transactions = transactions
        self.customers = customers
        self.address = address

    def get_bank_info(self):
        return {
            "Bank Number": self.bank_num,
            "Branch": self.branch,
            "Total Balance": self.total_balance,
            "Transactions": self.transactions,
            "Customers": self.customers,
            "Address": self.address
        }
    def add_transaction(self, amount):
        self.transactions.append(amount)
        self.total_balance += amount
    def add_customer(self, customer_name):
        self.customers.append(customer_name)
    def update_address(self, new_address):
        self.address = new_address                 


