def double(number):
    return number * 2

print(double(5))

# Now we will see it's modify face called lambda function

double = lambda number : number * 2
print(double(12))

add = lambda x,y : x + y
print(add(10,12))

lst = [10,20,30,40,50]

double = map(lambda x : x *2, lst)
print(list(double))



squire = map(lambda x : x * x, lst)
print(list(squire))
     
list_of_dicts = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Tanzim", "age": 50},
    {"name": "Mr Been", "age": 45}
]

juniors = filter(lambda person : person['age'] < 40, list_of_dicts)
print(list(juniors))
