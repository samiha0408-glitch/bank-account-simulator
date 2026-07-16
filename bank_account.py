class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.transaction_count = 0
    def deposit(self,amount):
        if amount <= 0:
            return False
        self.balance += amount
        self.transaction_count += 1
        return True
        
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_count += 1
            return True
        else:
            return False


