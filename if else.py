
Number = int(input("Enter a Number : "))
if Number >= 0 :
    print("Positive")
else:
    print("Negative")

a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))

if a>b and a>c:
    print("A is Big")
elif b>c:
    print("B is Big")
else:
    print("C is Big")

# even or odd
Num = int(input("Enter Number "))
if Num % 2 == 0 :
    print("It is Even Number")
else:
    print("It is Odd Number")

# For work
age = int(input("Enter age "))
if age>=18 and age<=60:
    print("Eligible to work")
else:
    print("Not Eligible to work")

# Validate Marks
marks = int(input('enter marks '))
if marks >= 0 and marks <= 100 :
    print('valid marks')
else:
    print('invalid marks')

# Gender check
gender = input("enter your gender ")
if gender=='m' or gender=='M' :
    print("Male")
else:
    print("Female")

# Vowel / consonant check
c = input("Enter Alphabet ")
if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' :
    print("It is Vowel ")
else:
    print("It is Consonant")

# Exam result
math = int(input("Enter Math Marks : "))
physics = int(input("Enter Physics Marks : "))
chem = int(input("Enter Chem Marks : "))
# passing marks = 45
if math >=45 and physics >=45 and chem >=45 :
    print("Passed")
else :
    print("Failed")

    a = int(input("Enter math marks : "))
    b = int(input("Enter chemitry marks : "))
    c = int(input("Enter physics marks : "))
    d = int(input("Enter english marks : "))
    e = int(input("Enter hindi marks : "))

    average = (a + b + c + d + e) / 5
    print("Average is ", average)

    if (average > 90 and average <= 100):
        print("Grade A+")
    elif (average <= 90 and average < 75):
        print("Grade B ")
    elif (average <= 75 and average < 60):
        print("Grade C ")
    elif (average <= 60 and average < 50):
        print("Grade D ")
    elif (average <= 50 and average < 33):
        print("Only Passed ")
    else:
        print("failed")

        age = int(input("Enter Your age : "))
        gender = input("Enter Your gender : ")

        if (age >= 18 and age < 30):
            if (gender == 'M' or gender == 'm'):
                print("day 700")
            elif (gender == 'F' or gender == 'f'):
                print("day 750")
        elif (age >= 30 and age <= 40):
            if (gender == 'M' or gender == 'm'):
                print("day 800")
            elif (gender == 'M' or gender == 'm'):
                print("day 850")

        else:
            print("wrong input")


