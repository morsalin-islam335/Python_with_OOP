# with open('message.txt','w') as file:
#     file.write("Python is a high level and object oriented programming language")  # write mode


# with open('message.txt','a') as file:
#     file.write("\nPython is a high level and object oriented programming language")   #append mode

with open('message.txt', 'r') as file:
    text = file.read()
    print(text)