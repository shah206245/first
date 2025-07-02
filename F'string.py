name = input("Enter your name : ")
age = int(input("Enter Your Age : "))
gender = input("Enter Your gender : ")
higher_qualification = input("Enter Your higher qualification : ")
# salary = int(input("Enter the salary : "))
# job_role=input("Enter job role : ")
# location = input("Enter location : ")
# company_name=input("Enter company name : ")




print(f"""\nHello!
My name is {name}.
And my age is {age}.
my gender is {gender}.
My higher qualification is {higher_qualification}.
""")


"""
name = input("What is your Name : ")
age = int(input("What is your age : "))
higher_qualification = input("What is your higher qualification : ")

# old style
"""
print("""\n Hello everyone !
My name is %s.
And my age is %d.
My higher qualification is %s"""%(name,age,higher_qualification))

# .format style
print("""\n Hello everyone !
My name is {}.
And my age is {}.
My higher qualification is {}.""".format(name,age,higher_qualification))

print("""\n Hello everyone !
My name is {a}.
And my age is {b}.
My higher qualification is {c}.""".format(a=name,b=age,c=higher_qualification))

# f string
print(f"""\n Hello everyone !
My name is {name}.
And my age is {age}.
My higher qualification is {higher_qualification}.""")
