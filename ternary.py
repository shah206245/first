a = int(input("Enter a number : "))
print("Even"if a%2==0 else"Odd")



a = int(input("\nEnter a : "))
b = int(input("Enter b : "))
diff = a-b if a > b else b-a
print(f"a is largest with diffrence {diff} "if a>b else f"b is largest with diffrence {diff}")



#swap
a = int(input("Enter a number : "))
b = int(input("Enter b number : "))
a,b = b,a
print("Swap a,b")
print(f"""a is {a}
b is {b}""")

