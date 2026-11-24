import math

class CalculatorError(Exception):
    pass

def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

def umnozh(a, b):
    return a*b

def delenie(a, b):
    if b==0:
        raise CalculatorError("Деление на ноль невозможно")
    return a/b

def step(a, b):
    return a**b

def kore(a):
    if a<0:
        raise CalculatorError("Корень из отрицательного числа не существует")
    return math.sqrt(a)

def factorial(n):
    if not isinstance(n, int):
        raise CalculatorError("Факториал определён только для целых чисел")
    if n<0:
        raise CalculatorError("Факториал отрицательного числа не существует")
    return math.factorial(n)

class Memory:

    def __init__(self):
        self._value=0

    def save(self, value):
        self._value=value
        return self._value

    def read(self):
        return self._value

    def add_to_memory(self, value):
        self._value+=value
        return self._value

    def clear(self):
        self._value=0
        return self._value