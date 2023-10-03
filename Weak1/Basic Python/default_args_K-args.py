def sum(num1, num2, num3 = 0):
    result = num1 + num2
    return result

total = sum(10,20)
print(total)

#args

def al_sum(*args):
    sum = 0
    for number in args:
        sum += number
    print(sum)

print( al_sum(10,20,39))  # args is work like tuple

