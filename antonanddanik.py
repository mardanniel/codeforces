num = input()
main = str(input())
count = [main.count("D"), main.count("A")]
if count[0] > count[1]:
    print("Danik")
elif count[0] < count[1]:
    print("Anton")
else:
    print("Friendship")
 