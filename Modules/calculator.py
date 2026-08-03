import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


def modulus(a, b):
    return a % b


def power(a, b):
    return a ** b


def square(number):
    return number ** 2


def cube(number):
    return number ** 3


def square_root(number):
    if number < 0:
        return "Square root of a negative number is not possible."
    return math.sqrt(number)


def maximum(a, b):
    return max(a, b)


def minimum(a, b):
    return min(a, b)
