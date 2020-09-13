num = int(input())
drinkp = list(map(int, input().split()))
print(100*(sum(drinkp)/(num*100)))