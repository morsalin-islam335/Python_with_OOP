#list comparehence

numbers = [10,20,30,0x31,33,55,70,32]
# odds = []
# for num in numbers:
#     if num % 2 == 1:
#         odds.append(num)



odds= [nums for nums in numbers if nums % 2 == 1 if nums % 5 == 0]  # we can do this with shortcut

print(odds)


players = ["sakib", "Tanzim sakib"]
ages = [30,24]

list_comprehension2 = [[player, age] for player in  players for age in ages]  # this will make nested list
print(list_comprehension2)
list_comprehension3 = [(player, age) for player in  players for age in ages]  # this will make list of tuple
print(list_comprehension3) 