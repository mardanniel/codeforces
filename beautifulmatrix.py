matrix = []
for i in range(5):
    matrix.append(list(map(int, input().split())))

for a in range(5):
    for b in range(5):
        if matrix[a][b] == 1:
            print(abs((3-(a+1)))+abs((3-(b+1))))

 