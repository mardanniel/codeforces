def sol(a ,b):
    if a.lower() < b.lower():
        return -1
    elif a.lower() > b.lower():
        return 1
    else:
        return 0
a = str(input())
b = str(input())
print(sol(a, b))
