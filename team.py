num = int(input())
mlist = []
gtwo = 0
for i in range(num):
    mlist.append(list(map(int, input().split())).count(1))
for j in range(num):
    if mlist[j] > 1:
        gtwo = gtwo + 1
print(gtwo)

