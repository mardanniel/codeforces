def func(num):
    if num % 2 == 0:
        return num/2
    else:
        return (num-1)/2-num

print(int(func(int(input()))))