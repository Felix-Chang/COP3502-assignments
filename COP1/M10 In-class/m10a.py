class Pakuri():
    def __init__(self, name):
        self.pakuri_name = name

    def attack(self, attack_name):
        print(f"{self.pakuri_name} used {attack_name}!")

    def speak(self):
        print(f"{self.pakuri_name}, {self.pakuri_name}!")

class BankAccount():
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        if amount < 0:
            print("Invalid amount.")
        else:
            print(f"Deposited ${amount}")
            self.balance += amount
    
    def withdraw(self, amount):
        if amount < 0:
            print("Invalid amount.")
        else:
            if amount > self.balance:
                print("You don't have enough money :(")
            else:
                print(f"Withdrew ${amount}")
                self.balance -= amount
    
    def display(self):
        print(f"Current balance: ${self.balance}")

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False
        
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"{(self.x, self.y)}"