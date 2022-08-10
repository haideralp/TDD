class BasicCalc:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2

    def dob(self, date, month):
        if date < 1:
            x_1 = int(input("Enter a date. "))
            x_2 = int(input("Enter a month. "))
            date, month = dob(x_1, x_2)
        return date, month
    def percentage(self, x1, x2):
        if x1 | x2 == 0:
            x1_1 = int(input("Enter a new number. "))
            x2_2 = int(input("Enter a new number. "))
            percentage(x1_1, x2_2)
        return 100 * x1 / x2 