size = list(map(int, input().split()))
right = True
for i in range(size[0]):
    if i % 2 == 0:
        print("#"*size[1])
    else:
        if right == True:
            print("."*(size[1]-1)+"#")
            right = False
        else:
            print("#"+(size[1]-1)*".")
            right = True