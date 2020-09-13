mylist = sorted(list(map(int, input().split("+"))))
ans = ""

for i in range(len(mylist)):
    if  i != len(mylist)-1:
        ans = ans + str(mylist[i]) + "+"
    else:
        ans = ans + str(mylist[i])

print(ans)