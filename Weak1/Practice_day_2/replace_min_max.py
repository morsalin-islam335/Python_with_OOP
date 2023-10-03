n = int(input())

array = list(map(int, input().split()))
max_index = array.index(max(array))
min_index = array.index(min(array))
array[max_index], array[min_index] = array[min_index], array[max_index]

for number in array:
    print(number,"", end = "")