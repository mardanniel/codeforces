a = list(map(int, input().split()))
am = 0
for i in range(1,a[2]+1):
    am = am + (i * a[0])
if a[1] >= am:
    print(0)
else:
    print(am - a[1])