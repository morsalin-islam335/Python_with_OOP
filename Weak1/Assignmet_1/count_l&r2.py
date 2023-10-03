#count L and R
string = input()
ans = []
string2 = ""; l = 0; r = 0

for char in string:
    string2 += char
    l = string2.count("L"); r = string2.count("R")
    if(l == r):
        ans.append(string2)
        string2 = ""
print(len(ans))
for answer in ans:
    print(answer)
