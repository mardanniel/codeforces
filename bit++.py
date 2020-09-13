num = int(input())
x = 0
for i in range(num):
    opr = input()
    if opr[1] == '+':
        x = x + 1
    else:
        x = x - 1
print(x)