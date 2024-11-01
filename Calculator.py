#Python Calculator

operator=input("Enter an operator (+ - * /): ")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the first number: "))
if operator=="+":
   print(num1+num2)
elif operator=="-":
   print(num1-num2)
elif operator=="*":
   print(num1*num2)
elif operator=="/":
   print(round(num1/num2, 2))
else:
   print(f"{operator} is not a valid operator.")
   