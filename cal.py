
import addition
import multiplication
num = input("""Select the operation :
      operation available : 
      1. Addition 
      2. Substraction
      3. Division
      4. Multiplication """)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

if num== "1":
    print( addition.addition(num1 , num2))
elif num == '4':
    print(multiplication.mul(num1 , num2))

