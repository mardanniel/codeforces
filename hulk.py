a = int(input())
phrase = []
for i in range(1, a+1):
    if i % 2 == 0:
        if i == a :
            phrase.append("I")
            phrase.append("love")
            phrase.append("it")
        else:
            phrase.append("I")
            phrase.append("love")
            phrase.append("that")
    else:
        if i == 0 or i == a:
            phrase.append("I")
            phrase.append("hate")
            phrase.append("it")
        else:
            phrase.append("I")
            phrase.append("hate")
            phrase.append("that")


print(" ".join(phrase))
