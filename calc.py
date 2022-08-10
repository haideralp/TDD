class BasicCalc:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2

    def dob(self,date,month):
         date = int(input("Enter a date: "))
         month = str(input("Enter a month: "))
         return date, month
    def percentage(self, x, y):
        if x | y == 0:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
        return x / y * 100
    def modulo(self,a,b):
        if a | b == 0
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
        return a % b

    def conversion(self, value1, value2):