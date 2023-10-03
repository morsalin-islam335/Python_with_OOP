# dictionary

persons = {'name': "Morsalin Islam", "roll": 6356}

print(persons["name"])
persons["age"] = 18
print(persons['age'])  #insert or add item

for keys, values in persons.items():
    print(keys, values)

print(persons.keys())
print(persons.values())


print(list(persons))

