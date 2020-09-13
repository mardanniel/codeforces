n = int(input())
cases = []
for i in range(n):
    cases.append(list(map(int, input().split())))
for j in range(len(cases)):
    if cases[j][0] % cases[j][1] == 0:
        print(0)
    else:
        print(cases[j][1]-cases[j][0]%cases[j][1])