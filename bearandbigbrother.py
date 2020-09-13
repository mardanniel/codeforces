weight = list(map(int, input().split()))
yearc = 0
while(weight[0] < weight[1] or weight[0] == weight[1]):
    yearc = yearc + 1
    weight[0] = weight[0] * 3
    weight[1] = weight[1] * 2
print(yearc)