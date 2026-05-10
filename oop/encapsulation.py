# Core Concept
# Unlike languages like Java, Python doesn't have strict private keywords.
# Instead, it uses naming conventions to indicate how attributes should be accessed:
# Public: No underscores (e.g., self.name). Accessible from anywhere.
# Protected: One underscore (e.g., self._salary). A hint to developers that it's internal.
# Private: Double underscores (e.g., self.__balance). Triggers "name mangling" to make external access harder.

# Example: Bank Account
# A common real-world example is a Bank Account, where the balance should only be changed through specific actions like depositing or withdrawing.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute (cannot be accessed directly)
    
    # String representation for easy debugging and display
    def __str__(self):
        return f"Account Holder: {self.owner}, Balance: {self.__balance}"
    
    # Getter: Safely retrieve the private balance
    def get_balance(self):
        return self.__balance

    # Setter: Modify balance with validation (Data Protection)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")


# Run below code to see the encapsulation in action using ipython interactive shell.
# Using the class
# account = BankAccount("Alice", 1000)

# Accessing public attribute
# print(account.owner)  # Output: Alice

# Attempting to access private attribute directly
# print(account.__balance)  # Raises AttributeError

# Correct way to interact via methods
# account.deposit(500)
# print(account.get_balance())  # Output: 1500
