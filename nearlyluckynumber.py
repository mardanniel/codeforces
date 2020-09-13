num = input()
seven = num.count('7')
four = num.count('4')
if seven + four == len(num) and seven > 0 and four > 0 or seven + four == 4 or seven + four == 7 or seven == 7 and four == 4:
    print('YES')
elif seven != 7 and four == 4 or seven == 7 and four != 4:
    print('NO')
else:
    print('NO')