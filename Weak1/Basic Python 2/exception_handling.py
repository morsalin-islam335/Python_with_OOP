# program to handle exception

a,b = map(int,input().split())

try:
    result = a / b  # if b = 0, that will be 0 division error
except:
    print("0 division error")
else:
    print(a/b)
finally:
    print("This is finally except")