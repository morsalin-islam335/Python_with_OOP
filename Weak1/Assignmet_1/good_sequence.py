n = int(input())
numbers = list(map(int, input().split()))
# print(arr)

frequency = dict()

# loop for first time initialize with 0
visited = dict()  # this is for keep track
for number in numbers:
    frequency[number] = 0
    visited[number] = False

for number in numbers:
    frequency[number] += 1
ans = 0
for number in numbers:
    if(frequency[number] > number and visited[number] == False):
        ans += frequency[number] - number
        visited[number] = True
    elif (frequency[number] < number and visited[number] == False):
        ans += frequency[number]
        visited[number] = True
print(ans)