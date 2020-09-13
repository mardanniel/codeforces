rooms = int(input())
available = 0
for i in range(rooms):
    chk = list(map(int, input().split()))
    if chk[0] + 2 <= chk[1]:
        available = available + 1
print(available)