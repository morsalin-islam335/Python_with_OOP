#set operation in python

n = int(input())
a = set()
print(type(a))

for i in range(n):
    a.add(int(input()))

print(a)

m = int(input())
b = set()
for i in range(m):
    b.add(int(input()))

print(a & b) # intersection
print(a | b) # union operation



a = {10,20,30}
b = {40,50,60}

print(a.union(b))
