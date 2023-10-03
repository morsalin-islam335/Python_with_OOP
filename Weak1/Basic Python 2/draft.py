# numbers = [10,20,30,40,50]
# numbers[1:4] = [20,14,36]
# print(numbers)


my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}

# Using get() to retrieve values
apple_count = my_dict.get('apple')
orange_count = my_dict.get('orange')

print(apple_count)  # Output: 3
print(orange_count)  # Output: None
