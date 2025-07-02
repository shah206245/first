# Temperature check)

temp = float(input("Enter Temperature : "))
if temp == 25:
    print("Normal")
else:
    if temp < 25:
        print("Cold")
    else:
        print("Hot")

            # OR

temp = float(input("Enter Temperature : "))

if temp == 25:
    print("Normal")

elif temp < 25:
    print("Cold")

else:
    print("Hot")


# discounted Bill
amt = float (input("Enter Bill Amount : "))
if amt < 1000:
    print("Discount Amount = ",amt * 0.1)
    total = amt - amt * 0.1
elif amt >= 1000 or amt < 5000 :
    print("Discount Amount = ", amt * 0.15)
    total = amt - amt * 0.15
elif amt >= 5000 or amt < 10000 :
    print("Discount Amount = ", amt * 0.2)
    total = amt - amt * 0.2
elif amt <= 10000 :
    print("Discount Amount : ", amt * 0.25)
    total = amt - amt * 0.25
print('Pay : ', total)


#  Day No to Day Name
day_no = int(input("Enter Day No ( 0 - 6 ) : "))

if  day_no == 0:
    print("Monday")
elif day_no == 1 :
    print("Tuesday")
elif day_no == 2:
    print("Wednesday")
elif day_no == 3:
    print("Thursday")
elif day_no == 4:
    print("Friday")
elif day_no == 5:
    print("Saturday")
elif day_no == 6:
    print("Sunday")
else:
    print("invalid day no")


#  Month No to Month Name
month_no = int(input("Enter Month No ( 0 - 11 ) : "))
if  month_no == 0:
    print("January")
elif month_no == 1 :
    print("February")
elif month_no == 2:
    print("March")
elif month_no == 3:
    print("April")
elif month_no == 4:
    print("May")
elif month_no == 5:
    print("June")
elif month_no == 6:
    print("July")
elif month_no == 7:
    print("August")
elif month_no == 8:
    print("September")
elif month_no == 9:
    print("October")
elif month_no == 10:
    print("November")
elif month_no == 11:
    print("December")
else:
    print("invalid Month no")



# Digit in Words
import random
digit = int(input("Enter Digit ( 0 - 9 ) : "))

if digit==0:
    print("Zero")
elif digit==1:
    print("One")
elif digit==2:
    print("Two")
elif digit==3:
    print("Three")
elif digit==4:
    print("Four")
elif digit==5:
    print("Five")
elif digit==6:
    print("Six")
elif digit==7:
    print("Seven")
elif digit==8:
    print("Eight")
elif digit==9:
    print("Nine")
else:
    print("invalid digit")

# Leap year
year = int(input("Enter year "))

if (year % 400 == 0) or  (year % 4 == 0 and year % 100!=0) :
    print("Leap year")
else:
    print("Not a Leap year")