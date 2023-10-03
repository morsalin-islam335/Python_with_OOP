
s = "hello_world"
print('lower ', s.lower())
print('upper ', s.upper())
print('capitalize ', s.capitalize())
print('casefold ',s.casefold())
print('title ',s.title())

print('swapcase ', s.swapcase())

ss = 'python is a high level and object oriented programming language'

print("center ", ss.center(8)) # this will print 8 index's sub-string to last sub-string
print("count ", ss.count('a'))
print("encode ", "hello programmer's".encode())

print("endswith ", ss.endswith("language"))

print("expandstab ", "hello\tptyhon programmers \tDo you\tEnjoy this language?".expandtabs(5))

s = 'dynamic programming is a core topic of programming'
print("find ", s.find("core")) # this will return specific index from finding string


#foramt method
print("We use python {} version".format("3.x"))

# format_map is like map but it used with  dictionary
name = "Morsalin"
passion = 'programming'

my_dict = {'name': "Morsalin Islam", "age": 18}

s = "hello this is {name} my age is {age}"
print(s.format_map(my_dict))

print("index method ", s.index('age'))


print("isdecimal method ","123".isdecimal())
print("isnumeric method ", "1234".isnumeric())

print("isprintable ", "python language".isprintable())
print("isupper ", "hey-siri".isupper())



from collections import Counter as ctr
text = "Python is invented by Guido Van Rosam"
print(ctr(text)) #this will work like frequency array  