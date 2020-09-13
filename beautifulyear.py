def sol(num):
    num = int(num) + 1
    word = "".join(set(str(num)))
    if len(word) != len(str(num)):
        return sol(int(num))
    else:
        return num

num = input()
print(sol(num))
