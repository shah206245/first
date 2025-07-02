a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if (a > b and a > c):
    if (b > c):
        print(" b is second largest")
    elif (c > b):
        print("c is second largest")

elif (b > a and b > c):
    if (a > c):
        print(" a is second largest")
    elif (c > a):
        print("c is second largest")

elif (c > a and c > b):
    if (b > a):
        print(" b is second largest")
    elif (a > b):
        print("a is second largest")



        a = int(input("Enter first side : "))
        b = int(input("Enter second side : "))
        c = int(input("Enter third side : "))

        if ((a + b) > c) or ((b + c) > a) or ((c + a) > b):
            print("it is triangle")
        else:
            print("pagal hai kya ")
            
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = int(input("Enter fourth number : "))

if a > b and a > c and a > d:
    if b > c and b > d:
        print("second largest", b)
    elif c > b and c > d:
        print("second largest", c)
    else:
        print("second largest", d)

elif b > a and b > c and b > d:
    if a > c and a > d:
        print("second largest", a)
    elif c > a and c > d:
        print("second largest", c)
    else:
        print("second largest", d)

elif c > b and c > d and c > a:
    if a > b and a > d:
        print("second largest", a)
    elif b > a and b > d:
        print("second largest", b)
    else:
        print("second largest", d)
elif d > b and d > c and d > a:
    if b > c and b > a:
        print("second largest", b)
    elif c > b and c > a:
        print("second largest", c)
    else:
        print("second largest", a)

a = int(input("Enter a number : "))
b = int(input("Enter b number : "))
c = int(input("Enter c number : "))
d = int(input("Enter d number : "))

if (a > b and a > c and a > d):
    if (b > c and b > d):
        second_largest = b
    elif (c > b and c > d):
        second_largest = c
    else:
        second_largest = d

elif (b > a and b > c and b > d):
    if (a > c and a > d):
        second_largest = a
    elif (c > a and c > d):
        second_largest = c
    else:
        second_largest = d

elif (c > a and c > b and c > d):
    if (a > b and a > d):
        second_largest = a
    elif (b > a and b > d):
        second_largest = b
    else:
        second_largest = d

else:
    if (a > b and a > d):
        second_largest = a
    elif (b > a and b > d):
        second_largest = b
    else:
        second_largest = c

print("second_largest ", second_largest)


a = int(input("Enter first numbers : "))
b = int(input("Enter second numbers : "))
c = int(input("Enter third numbers : "))
d = int(input("Enter fourth numbers : "))

print("Descending Order : ")

if a > b > c > d:
    print(a, b, c, d)
elif a > b > d > c:
    print(a, b, d, c)
elif a > c > b > d:
    print(a, c, b, d)
elif a > c > d > b:
    print(a, c, d, b)
elif a > d > b > c:
    print(a, d, b, c)
elif a > d > c > b:
    print(a, d, c, b)

elif b > c > d > a:
    print(b, c, d, a)
elif b > c > a > d:
    print(b, c, a, d)
elif b > d > c > a:
    print(b, d, c, a)
elif b > d > a > c:
    print(b, d, a, c)
elif b > a > c > d:
    print(b, a, c, d)
elif b > a > d > c:
    print(b, a, d, c)

elif c > a > b > d:
    print(c, a, b, d)
elif c > a > d > b:
    print(c, a, d, b)
elif c > b > a > d:
    print(c, b, a, d)
elif c > b > d > a:
    print(c, b, d, a)
elif c > d > a > b:
    print(c, d, a, b)
elif c > d > b > a:
    print(c, d, b, a)

elif d > a > b > c:
    print(d, a, b, c)
elif d > a > c > b:
    print(d, a, c, b)
elif d > b > c > a:
    print(d, b, c, a)
elif d > b > a > c:
    print(d, b, a, c)
elif d > c > b > a:
    print(d, c, b, a)
elif d > c > a > b:
    print(d, c, a, b)


# student challenges
# discounted Bill

amt = float (input("Enter Bill Amount : "))
if amt < 1000:
    print("you get a discount of : 10%")
    print("Discounted Amount is : ",amt * 0.1)
    total = amt - amt * 0.1
elif amt >= 1000 or amt < 5000 :
    print("you get a discount of : 15%")
    print("Discounted Amount is : ", amt * 0.15)
    total = amt - amt * 0.15
elif amt >= 5000 or amt < 10000 :
    print("you get a discount of : 20%")
    print("Discounted Amount is : ", amt * 0.2)
    total = amt - amt * 0.2
elif amt <= 10000 :
    print("you get a discount of : 25%")
    print("Discounted Amount is : ", amt * 0.25)
    total = amt - amt * 0.25
print('Net Payable amount is : ', total)


card = int(input("Enter Delivered Card : "))
salary = float(input("Enter Your salary  : "))

if card > 0 and card < 10 :
    print("Sorry Better luck but next time : ")
    print("your Total Salary is : ",card*500)
elif card >=10 and card < 20 :
    print("Sorry Better luck but next time : ")
    print("your Total Salary is : ",salary)
elif card >= 20 and card < 25:
    print("Your incentive is : 3000")
    print("Your Total salary is : ",salary + 3000)
elif (card >= 25 and card < 30) :
    print("Your incentive is : 5500")
    print("Your Total salary is : ",salary + 5500)
elif (card >= 30 and card < 35) :
    print("Your incentive is : 8000")
    print("Your Total salary is : ", salary + 8000)
elif (card >= 35 and card < 45) :
    print("Your incentive is : 11000")
    print("Your Total salary is : ", salary + 11000)