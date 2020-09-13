constraints = list(map(int, input().split()))
scores = list(map(int, input().split()))
count = 0
for i in range(constraints[0]):
    if scores[i] > constraints[1] or scores[i] == constraints[1]: 
        count = count + 1
print(count)
