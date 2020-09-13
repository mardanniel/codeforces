string = input()
ans = []

def isvowel(a):
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        return True
    else:
        return False
for letter in string:
    if isvowel(letter.lower()):
        pass
    else:
        ans.append(letter.lower())
ans = "."+".".join(ans)
print(ans)