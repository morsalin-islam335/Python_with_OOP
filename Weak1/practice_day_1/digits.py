#program to extract digit

test = int(input())

for i in range(test):
    digit = int(input())
    if digit == 0:
        print(0)
    else:

        numbers = []
        while digit > 0:
            numbers.append(digit % 10)
            digit //= 10
        for i in range(0, len(numbers),1):
            print(numbers[i],'',end = "")
        print()
