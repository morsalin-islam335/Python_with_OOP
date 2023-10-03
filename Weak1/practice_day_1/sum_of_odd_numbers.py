test = int(input())

for i in range(test):
    # x = int(input()); y = int(input())
    x,y = map(int,input().split())

    ans = 0
    for j in range(min(x,y)+1, max(x,y), +1):
        if(j % 2 !=  0):
            ans += j
    print(ans)
