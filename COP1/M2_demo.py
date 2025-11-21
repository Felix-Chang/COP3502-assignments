'''
example of mutability

a = 201
print(id(a))
print(type(a))

a += 1

print(id(a))
print(type(a))'''



'''
Number Swapping example

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

num1, num2 = num2, num1

OR YOU COULD DO THIS

a = a + b
b = a - b
a = a - b

print("After swapping:", f"First number = {num1}, Second number = {num2}")
'''



import math

print("Enter coordinates for point 1")
x1 = int(input("X1: "))
y1 = int(input("Y1: "))

print("Enter coordinates for point 2")
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

delta_x = math.fabs(x1-x2)
delta_y = math.fabs(y1-y2)

straight_line_distance = math.sqrt(delta_x**2 + delta_y**2)

manhattan_distance = delta_x + delta_y

midpoint = (f"{(x1+x2) / 2}", f"{(y1+y2) / 2 }")

print(f"{straight_line_distance:.2f}")
print(f"{manhattan_distance:.2f}")
print(midpoint)


