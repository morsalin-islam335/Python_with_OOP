# This program objective is to know about decorator
import math
def timer(fun):
    
    def inner(*args, **kwargs):
            
        print("start")
        fun(*args, **kwargs)
        print('end')
    
    return inner



@timer
def get_factorial(n):
    fact = math.factorial(n)
    print(f"factorial of {n} is {fact}")


get_factorial(10)

# import time
# print(time.time())



