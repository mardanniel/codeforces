num = int(input())
colr = list(str(input()).strip())
count = 0
for i in range(num-1):
    if colr[i] == colr[i+1]:
        count = count + 1
print(count)