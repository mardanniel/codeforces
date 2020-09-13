num = list(map(int, input().split()))
for i in range(num[1]):
    if num[0] % 10 == 0:
        num[0] = num[0] / 10
    else:
        num[0] = num[0] - 1
print(int(num[0]))