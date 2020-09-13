top = input()
bot = input()
ans = []
for i in range(len(top)):
    if top[i] == bot[i]:
        ans.append("0")
    else:
        ans.append("1")
print("".join(ans))