# d = {1:'one',2:"two",3:"three",4:'four'}

                        # creations
# # iterable pairs
# d = [(1,"one"),(2,"two"),(3,"three"),(4,"four")]
# print(dict(d))

# # zip function
# l1 = [1,2,3,4,5]
# l2 = ['one','two','three','four']
# d = zip(l1,l2)
# print(dict(d))

# # enumerate function
# l = ['one','two','three','four']
# print(dict(enumerate(l,1)))

                        # comprehensions
# #iterable pairs
# l = [(1,"one"),(2,"two"),(3,"three"),(4,"four")]
# print({x:y for x,y in l})

# # zip function
# l1 = [1,2,3,4]
# l2 = ['one','two','three','four']
# print({x:y for x,y in zip(l1,l2)})

# # enumerate function
# l = ['one','two','three','four']
# d = {x:y for x,y in enumerate(l,1)}
# print(d)
# print(d.setdefault(10))
# print(d)
# print(d.setdefault(8,"eight"))
# print(d)

# d = {}
# num = int(input("Enter a number : "))
#
# for i in range(num):
#     k = input("Enter name : ")
#     v = int(input("Enter marks : "))
#     d[k]=v
# print(d)
#
# new  = input("Enter Key : ")
# if new in d:
#     newv = int(input("Enter New Value : "))
#     d[new]=newv
# else:
#     print("Key Not found")
# print(d)



# a = 52
# print("start {0:>15b} end".format(a))
# shah = {}
# shah["Name"]= "Shah Hasan"
# shah['marks']=588
# shah['percentage']=91.5
# print(shah)

# del shah["marks"]
# print(shah)
# del shah
# print(shah)
# shah.clear()
# print(shah).

# hasan = shah.copy()
# print(shah)
# print(hasan)

# dic = {'Name': 'Shah Hasan', 'marks': 588, 'percentage': 91.5}
# print(dic.get('Name'))
# print(dic.get("age"))
# print(dic.get('value','not available'))

# print(dic.items())
# for k,v in dic.items():
# print(k," = ",v)

# dic['Name']='SHAH HASAN'
# keys = [10,20,30,40,50]
# j = j.fromkeys(keys,0)
# print(j)
#
# print(dic.items())
# for k,v in dic.items():
#     print(k," = ",v)


# d = {}
# num = int(input("Enter a number : "))
# for i in range(num):
#     k = input("Enter name : ")
#     v = int(input("Enter Marks : "))
#     d[k]=v
# print(d)
# det = input("Enter Key: ")
# if det in d:
#     del d[det]
# print(d)


# ds = {}
# a = int(input("Enter a number : "))
# for i in range(a):
#     k = input("Enter Key : ")
#     v = int(input("Enter Value : "))
#     ds[k] = v
# print(ds)




# nk = input("Enter new key : ")
# if nk in ds:
#     nv = input("Enter new value : ")
#     ds[nk] = nv
#     print(ds)
# else:
#     print("Not found")

# s =  input("Enter search : ")
# if s in  ds:
#     del ds[s]
# print(ds)

# l =  [3,9,5,8,10]
# l.extend(range(8,10))
# print(l)

