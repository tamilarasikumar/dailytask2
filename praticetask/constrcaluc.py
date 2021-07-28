class Calculator:
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b
    def floor(self,a,b):
        return a//b
 
myCalculator = Calculator()
a=int(input("Enter the 1st num:"))
b=int(input("Enter the 2nd num:"))
print(myCalculator.addition(a,b))
print(myCalculator.subtraction(a,b))
print(myCalculator.multiplication(a,b))
print(myCalculator.division(a,b))
print(myCalculator.floor(a,b))