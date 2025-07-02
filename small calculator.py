a = int(input("Enter a number : "))
ope = input("enter operator : ")
b = int(input("Enter b number :"))
# user=input("enter 'y' for yes 'n' for no ")
if ope=='+':
    print(a+b)
elif ope=='-':
    print(a-b)
elif ope=='*':
    print(a*b)
elif ope=='/':
    print(a/b)

user=input("enter 'y' for yes 'n' for no ")
while user=='y' or user=='Y':
    a = int(input("Enter a number : "))
    ope = input("enter operator : ")
    b = int(input("Enter b number : "))

    if ope == '+':
        print(a + b)
    elif ope == '-':
        print(a - b)
    elif ope == '*':
        print(a * b)
    elif ope == '/':
        print(a / b)
    user = input("enter 'y' for yes 'n' for no ")
else:
    print('thank you for submission')