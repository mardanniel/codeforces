num = int(float(input()))
words = []
for i in range(num):
    words.append(str(input()))
    if len(words[i]) > 10: 
        words[i] = words[i][0] + str(len(words[i]) - 2) + str(words[i][len(words[i])-1])
    else:
        pass
for j in range(len(words)):
    print(words[j])
