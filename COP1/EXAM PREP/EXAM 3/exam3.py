class Gradebook:
    def __init__(self, grades):
        self.grades = grades

    def averages(self):
        mean = sum(self.grades)/len(self.grades)
        return (mean, self.find_median())
    
    def find_median(self):
        self.grades.sort()
        n = len(self.grades)
        if n % 2 == 0: # even length
            median = (self.grades[n/2 - 1] + self.grades[n/2]) / 2
        else: # odd length
            median = self.grades[n//2]
        return median
    
# list_of_grades = [80, 90, 94]
# gradebook = Gradebook(list_of_grades)
# print(gradebook.averages())

class Airplane:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

class AirportLog(Airplane):
    def __init__(self):
        self.logbook = {}
    def add_airplane(self, time, model, capacity):
        if not self.logbook.get(time, None):
            self.logbook[time] = []
        self.logbook[time].append(Airplane(model, capacity))
    def print_airplanes_at_time(self, time):
        for plane in self.logbook.get(time, []):
            print(plane.model, end=" ")
        print()

# Test case 1:

# port = AirportLog()
# port.add_airplane(1, "delta", 40)
# port.add_airplane(1, "disney", 100)
# port.print_airplanes_at_time(1)

# Test Case 2:

# port = AirportLog()

# port.add_airplane(1, "delta", 40)
# port.add_airplane(2, "disney", 100)
# port.add_airplane(3, "world", 100)
# port.add_airplane(3, "hello", 100)

# port.print_airplanes_at_time(3) 

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, miles_per_gallon):
        super().__init__(make, model, year)
        self.miles_per_gallon = miles_per_gallon
    def display_info(self):
        super().display_info()
        print(f"Miles per Gallon: {self.miles_per_gallon}")

class Book:
    count = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = Book.count + 1
        Book.count += 1

    def get_info(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}"
    
    @staticmethod
    def is_classic(title):
        return "a" in title.lower()

    @classmethod
    def get_num_books(cls):
        return cls.count
    
class FictionBook(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre
    def get_info(self):
        return f"{super().get_info()}, Genre: {self.genre}"

class NonFictionBook(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.subject = subject
    def get_info(self):
        return f"{super().get_info()}, Subject: {self.subject}"
    
#Test Case 1:

# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
# print(book1.get_info())
# book2 = Book("The Hunger Games", "Suzanne Collins")
# print(book2.get_info())
# print("Number of Books:", Book.get_num_books())

# Test case 2

# fiction_book1 = FictionBook("1984", "George Orwell", "Dystopian")
# print(fiction_book1.get_info())
# print("Is Classic:", Book.is_classic(fiction_book1.title))

# Test case 3

# nonfiction_book1 = NonFictionBook("A Brief History of Time", "Stephen Hawking", "Science")
# print(nonfiction_book1.get_info())
# print("Is Classic:", Book.is_classic(nonfiction_book1.title))

class Student:
    def __init__(self, name, savings, college):
        self.name = name
        self.savings = savings
        self.college = college
    def pay_tuition(self):
        if self.savings >= 20_000:
            self.savings -= 20_000
            print("You have successfully paid your tuition!")
        else:
            self.savings -= 20_000
            print("You do not have enough savings to pay your tuition.")
    def print(self):
        print(f"Student Name: {self.name}")
        print(f"Student Savings: {self.savings}")
        print(f"Student University: {self.college}")

# Test Case 1:
# student = Student("Tonya", 20000, "UF")
# student.pay_tuition()
# student.pay_tuition()
# student.print()

# Test Case 2:
# student = Student("John", 240000, "FSU")
# student.pay_tuition()
# student.pay_tuition()
# student.print()

class ToDoList:
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task):
        self.tasks[task] = False
    
    def complete_task(self, task):
        if task not in self.tasks:
            print("error no such task")
        else:
            self.tasks[task] = True
    
    def display_tasks(self):
        for task, status in self.tasks.items():
            print(f"{task}: ", end="")
            if status:
                print("Completed")
            else:
                print("not completed")

# test case 1

# my_todo_list = ToDoList()
# my_todo_list.add_task("Buy groceries")
# my_todo_list.add_task("Wash the car")
# my_todo_list.display_tasks()
# my_todo_list.complete_task("Buy groceries")
# my_todo_list.display_tasks()

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeBook(Recipe):
    def __init__(self, recipes=[]):
        self.recipes = recipes

    def add_recipe(self, name, ingredients, instructions):
        self.recipes.append(Recipe(name, ingredients, instructions))

    def find_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                print(f"Ingredients: {", ".join(recipe.ingredients)}")
                print(f"Instructions: {recipe.instructions}")
                return
        print("Recipe not found")

# Test case 1:

# recipe_book = RecipeBook()
# recipe_book.add_recipe("Pancakes", ["flour", "eggs", "milk"], "Mix all ingredients and fry.")
# recipe_book.find_recipe("Pancakes")

# # Test Case 2:
# recipe_book = RecipeBook()
# recipe_book.add_recipe("Pancakes", ["flour", "eggs", "milk"], "Mix all ingredients and fry.")
# recipe_book.find_recipe("Waffles")


'''Algorithms Practice Section'''

'''
Linear Search

def linear_search(items, key):
    for item in items:
        if item == key:
            return True
    return False

print(linear_search([1, 2, 5, 3, 10], 3))
'''

'''
Binary Search

def binary_search(items, key):
    start = 0
    end = len(items) - 1

    while start <= end:
        mid = (start + end) // 2

        if items[mid] == key:
            return mid
        
        elif items[mid] > key:
            end = mid - 1
        
        elif items[mid] < key:
            start = mid + 1

    return -1

print(binary_search([1, 2, 5, 3, 10], 8))
'''

'''
Selection Sort
def selection_sort(items):
    n = len(items)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j
    
        items[i], items[min_index] = items[min_index], items[i]

    return items

print(selection_sort([4, 1, 7, 10, 5, 2]))
'''

'''
Bubble Sort
def bubble_sort(items):
    n = len(items)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

print(bubble_sort([10, 5, 15, 20, 1, 9]))'''

