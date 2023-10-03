n = int(input())
 
s = list(input().split())
s2 = s[::-1]
if(s == s2):
    print("YES")
else:
    print("NO")