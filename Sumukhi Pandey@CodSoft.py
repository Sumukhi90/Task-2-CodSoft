# Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and an operation choice. Perform the calculation 
and display the result.

#Building a simple calculator performing arithmetic operations.
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
    
print("Select an operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice=int(input("Choose operations from 1, 2, 3, 4 "))
if choice==1:
    print("x","+","y","=",add(x,y))
elif choice==2:
    print("x","-","y","=",subtract(x,y))
elif choice==3:
    print("x","*","y","=",multiply(x,y))
elif choice==4:
    print("x","/","y","=",divide(x,y))
else:
    print("Invalid input")
choice=input("Enter yes to proceed and no to terminate:")
if choice=="yes":
    print("Proceed")
else:
    print("Terminate")
