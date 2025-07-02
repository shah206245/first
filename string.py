#  -10987654321
s = "shah hasan"
#    0123456789 = 10 letters

                # indexing
"""
# start stop
print(s[:])
print(s[4:])
print(s[:4])
print(s[-5:])
print(s[-9:])
print(s[1:-1])
print(s[1:40])
print(s[40:40])
print(s[1:1])

# start stop step
print(s[::2])
print(s[4::1])
print(s[:4:2])
print(s[-5::-1])
print(s[-9::5])
print(s[1:8:3])
print(s[1::2])
print(s[::1])

                    # Traverrsing
for i in s:
    print(i)

for i in range(len(s)):
    print(s[i])

                    # Concatenation (+)
print(s + " 456")
print(s + " ansari")
print(s + " @")
                    # Repetation (*) we can use only int value
print(s*3)
                    # Membership (in , not in)
print("h" in s)
print("k" in s)
print("K" not in s)
print(not("l" in s))

                    # string comparision (depend on ASCII value)
                            # a - z = 97 - 122
                            # A - Z = 65 - 90
                            # 0 - 9 = 48 - 57
print("shah">'25')
print("HASAN">'shah')
print(not('hasan'<'1'))

# find = left to right
print(s.find('h',2,8))      # it give a first index when it start
print(s.find('a'))
print(s.find('l')) # -1 mean latter not found in string

# r find = right to left
print(s.rfind('h',2,8))      # it give a first index when it start
print(s.rfind('a'))
print(s.rfind('l')) # -1 mean latter not found in string

# index = left to right
print(s.index('n'))
# print(s.index('t')) # it is provide error when str not found

# rindex = right to left
print(s.rindex('n'))
# print(s.rindex('t')) # it is provide error when latter not found

# count
print(s.count('s'))
print(s.count('h',1,8))
print(s.count('t')) # 0 mean latter not in string


                    # alignment & padding (add char)

print(s.ljust(13,"*")) # left justify
print(s.rjust(13,"-")) # right justify
print(s.center(13,"#")) # center
print(s.zfill(13)) # 0 fill,
"""


                    # strip method (remove char) it can't remove char in middle of string

"""
c1 = "###shah hasan"
c2 = "*shah hasan*"
c3 = "@#!$shah hasan#!_@$"
print(c1.strip('#'))
print(c2.strip('*'))
print(c3.strip('@3$!#_'))
print(c3.lstrip('#@!$')) # lstrip = remove only left side 
print(c3.rstrip('@_!$#')) # rstrip = remove only right side 
"""

                   # replace
"""
l = "shah hasan"
print(l.replace(" ",'@'))
print(l.replace('h',"H",2))
"""

                   # join
"""                   
h1 = 'Shah'
h2 = '##'
print(h2.join(h1))
print(h1.join(h2))

h3 = ' Pyhton '
h4 = ' java '
print(h3.join(h4))
print(h4.join(h3))
"""

                    # split = remove letter or otherthing
"""
n = "shah hasan ansari"
print(n.split()) # by default space remove
print(n.split('a')) # by default all
print(n.split("a",2)) # maxsplit = how many time split

# rsplit = remove from left to right
print(n.rsplit("a",))
print(n.rsplit("h",3))
"""
                    # startswith = True / False
"""                    
j = "i am good person"
print(j.startswith('i'))
print(j.startswith(' i am')) # start width space
print(j.startswith('am'))
                    # endswith = True / False
print(j.endswith('n'))
print(j.endswith('person ')) # end with space
print(j.endswith('perso'))
                    # removeprefix = remove letter or character when startswith is True
print(j.removeprefix("i "))
print(j.removeprefix(' i am'))
print(j.removeprefix(' i am')) # startswith is False = return string
                    # removesuffix = remove letter or character when endswith is True
print(j.removesuffix('n'))
print(j.removesuffix('person '))
print(j.removesuffix("perso"))
"""
                   # partition = it divide a string in three part
"""
m = "python is a good language"
print(m.partition('o'))
print(m.partition("g"))

                    # rpartition = right to left
print(m.rpartition('o'))
print(m.rpartition('n'))
"""

                    # Case convesion
'''
w = "shah hasan"
print(w.capitalize()) # only first latter is capitalize
print(w.upper()) # convert all to upper case
print(w.lower()) # convert all to lower case
print(w.title()) # every first latter is capital
print(w.swapcase()) # convert upper to lower , lower to upper
print(w.casefold()) # it is same as lower case
'''

                    # Inquiry methods = True or False
b = "Shah"
print(b.isalpha()) # only alphabet
print(b.islower()) # only lowercase alphabet
print(b.isupper()) # only uppercase alphabet
print(b.title()) # only title case alphabet

print()