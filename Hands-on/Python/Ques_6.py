m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in m:
    m[2], m[0] = m[0], m[2]
    for j in i:
        i[2], i[0] = i[0], i[2]

for i in range(3):
    for j in range(3):
        print(m[i][j], end='\t')
    print()