levels = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
temp = []
for i in range(1,X[0]+1):
    temp.append(X[i])
for j in range(1,Y[0]+1):
    temp.append(Y[j])
temp = sorted(set(temp))
total = levels*(levels+1) / 2
sumoftemp = sum(temp)
if total - sumoftemp > 0:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")


    


