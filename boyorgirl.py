a = str(input())
surv = len(list(dict.fromkeys(a)))
if surv % 2 == 0: 
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")