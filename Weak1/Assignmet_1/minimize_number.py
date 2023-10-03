# minimum number of divide
n = int(input())
array = list(map(int,input().split()))

arr2 = array
ans = 0
while(True):
    flag = True
    for index, value in enumerate(array):
        if flag == False:
            break
        elif (value % 2 != 0):
            flag = False
            break
        else:
            array[index] /= 2

    if(flag != False):
        ans += 1
    else:
        break
    
print(ans)
