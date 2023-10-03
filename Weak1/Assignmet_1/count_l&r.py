str = input()
items = []

count = 0
if str[0] == "L":
    for char in str:
        if char == 'L':
            count += 1
        elif count != 0 :
            items.append(count)
            count = 0

    print(len(items))

    for L_and_R in items:
        print(L_and_R * "L", L_and_R *"R", sep = "")

else:
    for char in str:
        if char == 'R':
            count += 1
        elif count != 0 :
            items.append(count)
            count = 0

    print(len(items))

    for L_and_R in items:
        print(L_and_R * "R", L_and_R *"L", sep = "")





# S = input()
# curr = ""
# count_l=0
# count_r =0
# b_string = []
# for string in S:
#     curr= curr+string
#     count_l = curr.count("L")
#     count_r = curr.count("R")
#     if count_l==count_r:
#         b_string.append(curr)
#         curr=""
#         count_l=0
#         count_r =0
# print(len(b_string))
# for string in b_string:
#     print(string)

S = input()#S
curr = ""
count_l=0
count_r =0
b_string = []
for string in S:
    curr= curr+string
    count_l = curr.count("L")
    count_r = curr.count("R")
    if count_l==count_r:
        b_string.append(curr)
        curr=""
        count_l=0
        count_r =0
print(len(b_string))
for string in b_string:
    print(string)