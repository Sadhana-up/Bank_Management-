from bank import Bank
from account import Account
from customer import Customer
from loan_management import Loan


def main():
    # Create a bank
    bank = Bank(bank_num=101, branch="Downtown", address="123 Main Street")

    # Create a customer
    customer = Customer(customer_id=1, name="Alice Johnson", email="alice@email.com", age=30, phone="555-1234")
    bank.add_customer(customer)

    # Create an account for that customer
    account = Account(account_id=5001, balance=1000, account_type="checking")
    customer.add_account(account)
    bank.add_account(account)

    # Deposit and withdraw money
    account.deposit(500)
    account.withdraw(200)

    # Create a loan for the customer
    loan = Loan(loan_id=1, account_id=5001, loan_type="Home Loan", amount=5000, interest_rate=0.05, term_years=2)
    customer.add_loan(loan)

    # Make a payment toward the loan
    loan.make_payment(1000)

if __name__ == "__main__":
    main()
