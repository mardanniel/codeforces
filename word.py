word = str(input())
count = [0, 0]
for letter in word:
    if letter.isupper():
        count[0] = count[0] + 1
    else:
        count[1] = count[1] + 1
if count[0] > count[1]:
    print(word.upper())
else:
    print(word.lower())        