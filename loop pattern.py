# 1
"""
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
a = int(input("Enter a number : "))
for i in range (1,a+1):
    for j in range(1,a+1):
        print("*",end=" ")
    print()"""

# 2
"""
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
a = int(input("Enter a number : "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#          or
for i in range (1,a+1):
    for j in range(1,a+1):
        if i>=j:
            print("*",end=" ")
    print()
#          or
for i in range(1,a+1):
    print("* "*i)"""

# 3
"""
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

a = int(input("Enter a number : "))
for i in range(a,0,-1):
    print('* '*i)
#           or
for i in range (1,a+1):
    print("* "*(a+1-i))
#           or
for i in range(1,a+1):
    for j in range(1,a+1-(i-1)):
        print("* ",end=" ")
    print()
#           or
for i in range(a,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()"""

# 4
"""
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
a = int(input("Enter a number : "))
for i in range(1, a + 1):
    for j in range(1, a + 1):
        if i <= j:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()
#           or
for i in range(1, a + 1):
    print("  " * (i - 1), end=" ")
    print("* " * (a - (i - 1)))"""

# 5
"""
 #         * 
 #       * * 
 #     * * * 
 #   * * * * 
 # * * * * * 
a = int(input("Enter a number : "))
for i in range(a+1,0,-1):
    print("  "*(i-1),end=" ")
    print("* "*(a-(i-1)))"""

# a = int(input("Enter a number : "))
# for i in range (a+1,0,-1):
#     print("  " * (i - 1), end=" ")
#     print("* "*(a - 1 - (i - 1)))




"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j, end=" ")
    print()
  
        
5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1 

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(i, end=" ")
    print()
 
5 
4 5 
3 4 5 
2 3 4 5 
1 2 3 4 5    
   
for i in range(a,0,-1):
    for j in range(i,a+1):
        print(j,end=" ")
    print()"""

"""        
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 

for i in range(1,6):
    for j in range(4,i-1,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
    
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5  

for i in range(1,6):
    for j in range(4,i-1,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(i,end=" ")
    print() 
    
        1 
      2 1 
    3 2 1 
  4 3 2 1 
5 4 3 2 1 

for i in range(1,6):
    for j in range(4,i-1,-1):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    print()

          5 
        5 4 
      5 4 3 
    5 4 3 2 
  5 4 3 2 1 

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(" ",end=" ")
    for k in range(5,5-i,-1):
        print(k,end=" ")
    print()
    
        5 
      5 4 
    5 4 3 
  5 4 3 2 
5 4 3 2 1 

for i in range(5,0,-1):
    for j in range(4,5-i,-1):
        print(" ",end=" ")
    for k in range(5,i-1,-1):
        print(k,end=" ")
    print()
    
        5 
      4 4 
    3 3 3 
  2 2 2 2 
1 1 1 1 1 

for i in range(5,0,-1):
    for j in range(4,5-i,-1):
        print(" ",end=" ")
    for k in range(5,i-1,-1):
        print(i,end=" ")
    print()
    
        5 
      4 5 
    3 4 5 
  2 3 4 5 
1 2 3 4 5 

for i in range(5,0,-1):
    for j in range(4,5-i,-1):
        print(" ",end=" ")
    for k in range(i,6):
        print(k,end=" ")
    print()
    """

"""
1  2  3  4  5
6  7  8  9
10 11 12
13 14
15

a = 1
for i in range(5,0,-1):
    for j in range(i):
        print(a,end=" ")
        a+=1
    print()
    """


"""
1
2  3
4  5  6
7  8  9  10
11 12 13 14 15

a = 1
for i in range(1,6):
    for j in range(i):
        print(a,end=" ")
        a+=1
    print()"""