num = int(input())
words = str(input())
if len(words) < 24:
    print("NO")
else:
    words = list(words.strip())
    words = [word.lower() for word in words]
    words = sorted(list("".join(set(words)).strip()))
    if len(words) == 26:
        print("YES")
    else:
        print("NO")