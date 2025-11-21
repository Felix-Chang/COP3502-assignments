from base_classes import *

class SecureAccount(Account):
    def __init__(self, password):
        self.password = password
        super().__init__()
    
    def get_balance(self, password):
        if password != self.password:
            print("Incorrect password")
        else:
            return super().get_balance()
    
    def deposit(self, amount, password):
        if password != self.password:
            print("Incorrect password")
        else:
            super().deposit(amount)

    def withdraw(self, amount, password):
        if password != self.password:
            print("Incorrect password")
        else:
            super().withdraw(amount)

class MemoryCalculator(Calculator):
    def __init__(self):
        self.prev = 0
        super().__init__()

    def add(self, x, y):
        if x == "RESULT":
            x = self.prev
        if y == "RESULT":
            y = self.prev
        self.prev = super().add(x, y)
        return self.prev

    def sub(self, x, y):
        if x == "RESULT":
            x = self.prev
        if y == "RESULT":
            y = self.prev
        self.prev = super().sub(x, y)
        return self.prev

        
class ImprovedFraction(Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)

    def add(self, other):
        if type(other) == int:
            return super().add(Fraction(other, 1))
        else:
            return super().add(other)
        
    def multiply(self, other):
        if type(other) == int:
            return super().multiply(Fraction(other, 1))
        else:
            return super().multiply(other)
        
    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.multiply(other)
    
    def __str__(self):
        return f"{super().get_numerator()}/{super().get_denominator()}"