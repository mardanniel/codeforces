num = int(input())
count = 0
while(num != 0):
    if num > 5:
        num = num - 5
    else:
        num = num - num
    count = count + 1
print(count)
