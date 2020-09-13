num = int(input())
x = 0
y = 0
z = 0
minimum = 0
for i in range(num):
    chk = list(map(int, input().split()))
    x = chk[0]
    y = chk[1]
    z = (y - x) + z
    if z > minimum:
        minimum = z 
print(minimum)

