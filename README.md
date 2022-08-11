# TDD - Test Driven Development

## What is TDD ?
- Test Driven Development is a practice where test cases are developed to specify and validate what the code will do. 
- In simple terms, test cases for each functionality are created and tested first and if the test fails then the new code is written in order to pass the test and making code simple and bug-free.

## Diagram - Showing TDD Cycle 
![image](https://user-images.githubusercontent.com/97620055/183910129-46da16fc-bff1-47eb-9bef-b551b9944762.png)

## Process of TDD
### The practice of TDD approach includes the following steps:
- Red : a test written for a code which fails. 
- Green : a code is then writtern so the test is passed.
- Refactor (Grey) : code optimisation occurs here. Code structure is being checked without changing original functionality of the code. The outcome of this stage         of this stage should produce perfectly written code.
- This process is a repeating cycle  for every piece of functionality in the projects. It allows full test code coverage. 

## Benefits of TDD ?

-  Better program design and higher code quality --> a very simple and readable code is delivered improving project desing and quality (no repeat codes). 
-  Detailed project documentation --> no need for heavy documentations as programmers specify the strict requirements. Includes all user actions likely to take place. 
-  TDD reduces the time required for project development --> having clean and error free code means you can save a lot of time in projects due to ease of use. 
-  Code flexibility and easier maintenance --> bug free and easier to introduce and reproduce. Can be easily read and understood by non-developers. 
-  With TDD you will get a reliable solution --> After refactoring, you and developer has transparency for the reliability of the code. You can be sure the solution works.
-  Save project costs in the long run --> Decreases costs on projects overall due to multiple benefits as dicussed above. (Code quality, Readable, Scalability)


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


# Create DOB function
# Create Percentage function
# Create cm to m function
# Create modulo function

    def dob(self,value1,value2):
        return f"Your DOB is {value1} / {value2}"
    def percentage(self, value1, value2):
        return value1/value2 * 100
    def conversion(self, value):
        return value/100
    def modulo(self, value1, value2):
        return value1 % value2

```
### Unit Tests

```python
from calc import BasicCalc
import unittest
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
        self.assertEqual(self.calc_obj.dob(15,7), "Your DOB is 15 / 7")

    def test_percentage(self):
        self.assertEqual(self.calc_obj.percentage(1, 2), 50)

    def test_conversion(self):
        self.assertEqual(self.calc_obj.conversion(100), 1)

    def test_modulo(self):
        self.assertEqual(self.calc_obj.modulo(5,3),2)
```
### Showcasing The Passing of Test Results 
![image](https://user-images.githubusercontent.com/97620055/184082729-a3a88534-6152-4e91-b958-0808845be2a3.png)
