clr = input()
temp = []
for i in range(len(clr)):
    if clr[i].isalpha():
        temp.append(clr[i])
print(len(set(temp)))