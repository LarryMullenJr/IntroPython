import os
import datetime

class BankAccount:
    account_counter = 1000  # Static counter to generate unique account numbers

    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = BankAccount.account_counter
        BankAccount.account_counter += 1
        self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"
        with open(self.filename, 'w') as f:
            f.write("Transaction History\n")
            f.write(f"{datetime.datetime.now()} - Account created with balance {self.balance}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._record_transaction(f"Deposited {amount}")
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self._record_transaction(f"Withdrew {amount}")
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

    def check_balance(self):
        return self.balance

    def get_account_number(self):
        return self.accountNumber

    def get_holder_name(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def get_transaction_history(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def _record_transaction(self, transaction):
        with open(self.filename, 'a') as f:
            f.write(f"{datetime.datetime.now()} - {transaction}. Balance: {self.balance}\n")

# Test the BankAccount class
def main():
    # Create multiple bank accounts
    account1 = BankAccount("JohnDoe", "Checking")
    account2 = BankAccount("JaneDoe", "Savings", 500)
    
    # Perform some transactions on account1
    account1.deposit(1000)
    account1.withdraw(200)
    account1.withdraw(1000)  # Should display insufficient funds message
    
    # Perform some transactions on account2
    account2.deposit(1500)
    account2.withdraw(100)
    
    # Check balances
    print(f"Account1 balance: {account1.check_balance()}")
    print(f"Account2 balance: {account2.check_balance()}")
    
    # Get account details
    print(f"Account1 Number: {account1.get_account_number()}")
    print(f"Account1 Holder: {account1.get_holder_name()}")
    print(f"Account1 Type: {account1.get_account_type()}")
    
    print(f"Account2 Number: {account2.get_account_number()}")
    print(f"Account2 Holder: {account2.get_holder_name()}")
    print(f"Account2 Type: {account2.get_account_type()}")
    
    # Print transaction histories
    print("Account1 Transaction History:")
    print(account1.get_transaction_history())
    
    print("Account2 Transaction History:")
    print(account2.get_transaction_history())

if __name__ == "__main__":
    main()