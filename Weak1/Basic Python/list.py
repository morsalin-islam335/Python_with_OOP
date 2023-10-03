# list, array, collection is same

numbers = [10,20,30,40,50,23]
#forward index 0,1,2,3,4,5
#reverse index -1,-2,-3,-4,-5,-6  from last to first

print(numbers[2]," ", numbers[-2])
#list(start : end)

print(numbers[2:5]) # access 2,3,4 index

#list(start: end : step)
print(numbers[1:5:1])
print(numbers[1:5:2])
print(numbers[5:2:-1])


print(numbers[:])#first to last index
print(numbers[:5]) #first to 4th index
print(numbers[1:]) #first index to last index

print(numbers[::-1]) # it will print reverse list