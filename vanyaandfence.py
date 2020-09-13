fandh = list(map(int, input().split()))
heights = list(map(int, input().split()))
for i in range(fandh[0]):
    if heights[i] > fandh[1]:
        heights[i] = 2
    else:
        heights[i] = 1
print(sum(heights))