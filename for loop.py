# # fibonacci  series
# a = int(input("Enter a number : "))
# f1 = 0
# f2 = 1
#
# for i in range(a+1):
#     print(f1)
#     fn = f1 + f2
#     f1 = f2
#     f2 = fn


"""
n = int(input("Enter number "))
i = 0
sum = 0
while i<n:
    i=i+1
    sum = sum + i

    print("Sum is : ",sum)
    """

# prime number check
"""a = int(input("enter a number : "))
count = 0
for i in range(1, a + 1):
    if (a % i == 0):
        count += 1

if (count == 2):
    print("prime number")
else:
    print("not prime number")"""


# print
a = int(input("Enter a number : "))
for i in range (1,a+1):
    print(i)

# number pattern
a = int(input("Enter a number : "))

for i in range (a+2):
    for j in range (1,i):
        print(j,end=" ")
    print()

# reverse number pattern
a = int(input("Enter a number : "))
for i in range (a,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

# sum of enter number
a = int(input("Enter a number : "))
sum = 0

for i in range(1, a + 1):
    sum += i
print("sum is ", sum)

# table
a = int(input("Enter a number who you needa create table : "))

for i in range (1,11):
    print(f"{a} x {i}= ",a*i)


# square of enter highest number to everyone
a = input("Enter a number : ")
count = len(a)
s = int(a)
for i in range(1,count+1):
    x = s%10
    q = x**count
    print(q)
    s = s//10
