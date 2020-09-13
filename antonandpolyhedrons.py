polyhedrons = { "Tetrahedron" : 4,
                "Cube" : 6,
                "Octahedron" : 8,
                "Dodecahedron" : 12,
                "Icosahedron" : 20
                }
n = int(input())
ph = []
for j in range(n):
    ph.append(input())
sumofph = 0
for i in range(len(ph)):
    sumofph = sumofph + polyhedrons.get(ph[i])
print(sumofph)