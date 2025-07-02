# table of n
"""n = int(input("Enter a number "))

while n > 0:
    r = n%10
    print(r)
    n = n//10"""

#digits of a number
"""a = int(input("Enter a number : "))

while (0<a):
    r = a%10
    print(r)
    a = a//10"""

# count the digits of a number
"""a = int(input("Enter a number : "))
i=0

while (0<a):
    i += 1
    a = a//10

print(i)"""


# sum of digits of a number
"""a = int(input("enter a number : "))
sum = 0
i=0
while (0<a):
    sum = sum + a%10
    a = a//10

print(sum)"""


# reverse of a number an chcek palindrmome
"""a = int(input("enter a number : "))
rev = 0
m=a
while (0<a):
    r = a%10
    rev = rev*10  + r
    a = a//10

if (m==rev):
    print("\nit is palindrome")
else:
    print("\nnot palindrome")"""

#sum of n numbers
"""a = int(input("enter a number : "))
sum = 0
i = 0

while (i < a):
    i += 1
    s=int(input("enter "))
    sum = sum + s

print("your enter number total sum is ",sum)"""

# numbers
"""n = int(input("Enter a number : "))
i = 0
while n > 0:
    i =  i + 1
    n = n // 10
    print("numbers of digit : ",i)"""

"""n = int(input("Enter a number : "))
sum = 0
while n>0:
    r = n % 10
    sum = sum + r
    n = n//10
    print("Sum of n digits ",sum)"""


a=1
sum  = 0

while (a<=10):
    sum = sum + a
    a+=1
    print(sum)
    if sum%2==0:
        print("even")
    else:
        print("odd")

name = input("Enter name : ")
print(f'good morning {name}')
user=input("can  you repeat this : y/n :")
while user=="y" or user=="Y":
        name = input("Enter name : ")
        print(f'good morning {name}')
        user=input("can  you repeat this : y/n :")
else:
    print("Thank you for your patience")