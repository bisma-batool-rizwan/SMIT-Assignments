from calculator import *
from greetings import welcome, goodbye
from constants import APP_NAME, VERSION, PI

print(APP_NAME)
print("Version:", VERSION)
print("Value of PI:", PI)

name = input("\nEnter your name: ")
welcome(name)

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("\n========== RESULTS ==========")
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
print("Modulus:", modulus(num1, num2))
print("Power:", power(num1, num2))
print("Square of First Number:", square(num1))
print("Cube of First Number:", cube(num1))
print("Square Root of First Number:", square_root(num1))
print("Maximum:", maximum(num1, num2))
print("Minimum:", minimum(num1, num2))

goodbye(name)
