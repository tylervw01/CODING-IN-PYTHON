#Question 1

class Account: # CLASS
    accounts_created = 0 # CLASS VARIABLE

    def __init__(self, name): # CONSTRUCTOR
        self.name = name # INSTANCE VARIABLE
        self.balance = 0 # INSTANCE VARIABLE
        Account.accounts_created += 1 # CLASS VARIABLE

    def deposit(self, amount): # METHOD
        self.balance += amount # INSTANCE VARIABLE
        print(f"Deposited {amount}. New balance is {self.balance}.") # PRINT

    def withdraw(self, amount): # METHOD
        if self.balance >= amount: # IF STATEMENT
            self.balance -= amount # INSTANCE VARIABLE
            print(f"Withdrew {amount}. New balance is {self.balance}.") # PRINT
        else: # ELSE
            print("Insufficient funds.") # PRINT
    def get_balance(self): # METHOD
        return self.balance # RETURN

account1 = Account("Adam") # OBJECT
account2 = Account("Eve") # OBJECT

account1.deposit(90580) # METHOD CALL
account2.deposit(13490) # METHOD CALL

account1.withdraw(456) # METHOD CALL
account2.withdraw(2250) # METHOD CALL

print(f"Account 1 balance: {account1.get_balance()}") # METHOD CALL
print(f"Account 2 balance: {account2.get_balance()}") # METHOD CALL
print(f"Total accounts created: {Account.accounts_created}") # METHOD CALL