#program to know about local and global variable
#we can access global variable in function without using global keyword but can't change without using global keyword
tk = 1000 # global

def local(taka):
    global tk
    tk = 400
    print(tk)

local(tk)
print(tk)