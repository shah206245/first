# li = [1,2,3,4,5]
# print(type(li))

# # heterogeneous
# lt = ["shah",15,20.5,True,2+3j]

# # mutable
# li = [1,2,3,4,5]
# li[2]=5
# print(li)

# # append
# li = [1,2,3,4,5]
# li.append(6)
# print(li)

# # remove
# li = [1,2,3,4,5]
# li.remove(2)
# print(li)

# indexing
# li = [1,2,3,4,5]
# print(li[4])

# # slicing
# li = [1,2,3,4,5]
# print(li[1:4:2])
# print(li[-5:-2])

# # concatenation (+)
# l1 = [1,5,9,7,6]
# l2 = [5,8,4]
# l3 = l1 + l2
# print(l3)]

# repetition (*)
# li = [1,8,6,7]
# lt = li*2
# print(lt)


"""# Traversals
l = [10,15,12,56,45]

# # for
# for i in l:
#     print(i)

# # for with range
# for i in range(len(l)):
#     print(i,l[i])

# # while
# i = 0
# while (i<len(l)):
#     print(l[i])
#     i+=1
"""
# l = [int(x) for x in "ab7*9@c" if x.isnumeric()]
# print(l)



                                    # list challenges
# calculating the salary
"""
work_hour = [int(x) for x in input("Enter work hour, seperated by spaces : ").split()]
wage = int(input("Enter of wage : "))
total = sum(work_hour)
salary = wage * total
print(salary)
"""
# removing the duplicate values
"""
l1 = [2,3,5,8,9,1,2,4,3,2,3]
l2 = []
for x in l1:
    if x not in l2:
        l2.append(x)
print(l2)
"""
# concatenating a list into a single number
"""
li = [3,5,10,7,12]
for x in li:
    print(x,end="")
             # or
s1 = ""
for i in li:
    s1 += str(i)
print(int(s1))
"""
# overlapping elements in two lists
"""
l1 = [10,2,4,5,8,6]
l2 = [6,21,9,8,32,10]
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)
"""
# occurrences of each item
"""
lit = ['A','B','C','D','A','E','A','B','A','D','B','D']
result = []
for i in lit:
    if i not in result:
        result.append(i)
        count = lit.count(i)
        result.append(count)
print(result)
"""
# adding two matrix
"""
l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l2 = [[5,6,7,8],[5,6,7,8],[5,6,7,8]]
l3 = []
for i in range(3): # range = rows
    s = []
    for j in range(4): # range = column
        r = l1[i][j] + l2[i][j]
        s.append(r)
    l3.append(s)
print(l3)
"""
# transpose matrix
"""
l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l2 = []
for i in range(4): # elements = column
    s = []
    for j in range(3): # elements = row
        t = l1[j][i]
        s.append(t)
    l2.append(s)
print(l2)
"""
# word starting with a given latter
"""
m = ['pizza','nuggets','burger','pasta','hotdog','noodles']
f = input("Enter a letter you need to find : ")
for i in m:
    if i.startswith(f):
        print(i)
"""