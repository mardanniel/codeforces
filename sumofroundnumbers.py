num = int(input())
inputs = []
for i in range(num):
    inputs.append(str(input()))
for j in range(num):
    default = 1
    contain = []
    contain.append(inputs[j][0] + "0" * (len(inputs[j]) - 1))
    for k in range(1,len(inputs[j])):
        if inputs[j][k] != "0":
            default = default + 1
            if len(inputs[j]) == 2:
                right = inputs[j][k] + ("0" * (len(inputs[j]) - (inputs[j].index(inputs[j][k]) + 2)))
                contain.append(right)
            else:
                right = inputs[j][k] + ("0" * (len(inputs[j]) - (inputs[j].index(inputs[j][k]) + 1)))
                contain.append(right)
    print(default)
    print(*contain, sep=" ")
