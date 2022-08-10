# TDD - Test Driven Development

## What is TDD ?
- Test Driven Development is a practice where test cases are developed to specify and validate what the code will do. 
- In simple terms, test cases for each functionality are created and tested first and if the test fails then the new code is written in order to pass the test and making code simple and bug-free.

## Diagram - Showing TDD Cycle 
![image](https://user-images.githubusercontent.com/97620055/183910129-46da16fc-bff1-47eb-9bef-b551b9944762.png)

## Benefits of TDD ?

-  Better program design and higher code quality
-  Detailed project documentation
-  TDD reduces the time required for project development
-  Code flexibility and easier maintenance
-  With TDD you will get a reliable solution
-  Save project costs in the long run


### Calculator Functions

``` Python
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
```
### Unit Tests

```python
class Calc_tests(unittest.TestCase):
    calc_obj = BasicCalc()
    def test_add(self):
        self.assertEqual(self.calc_obj.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.calc_obj.subtract(8, 5), 3)

    def test_multiply(self):
        self.assertEqual(self.calc_obj.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(self.calc_obj.divide(10, 5), 2)

    def test_dob(self):
        self.assertIs(self.calc_obj.dob(date, month), date, month)
```