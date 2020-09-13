num = int(input())
mags = [None] * num
for i in range(num):
    mags[i] = str(input())
check = mags[0]
count = 0
for j in range(len(mags)):
    if check != mags[j]:
        check = mags[j]
        count = count + 1
    else:
        continue
print(count+1)