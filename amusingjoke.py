words = []
for i in range(3):
    words.append(input())
combined = words[0]+words[1]
combined = "".join(sorted(combined))
basis = "".join(sorted(words[2]))
if combined == basis:
    print("YES")
else:
    print("NO")