# what is inheritance in OOP?
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.

# Banking example of Inheritance in Python

# Base class (Parent class)
class BankAccount:
    
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient funds.")

        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def __str__(self):

        return (
            f"Account Number: {self.account_number}, "
            f"Balance: {self.get_balance()}"
        )


class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance, interest_rate):

        super().__init__(account_number, balance)

        self.interest_rate = interest_rate

    def add_interest(self):

        old_balance = self.get_balance()

        interest = old_balance * self.interest_rate / 100

        self.deposit(interest)

        new_balance = self.get_balance()

        print(
            f"Added interest: {interest}\n"
            f"Old balance: {old_balance}\n"
            f"New balance: {new_balance}"
        )
        return new_balance

    def __str__(self):

        return (
            super().__str__()
            + f", Interest Rate: {self.interest_rate}%, \nNew Balance: {self.add_interest()}"
        )