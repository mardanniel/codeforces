word = ["",""]
word[0] = input()
word[1] = input()
if "".join(list(reversed(word[0]))) == word[1]:
    print("YES")
else:
    print("NO")
 