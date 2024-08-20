def get_matrix(n, m, valu):
    matrix = []
    matrix.append(n)
    matrix.append(m)
    matrix.append(valu)
    for i in range(n):
        matrix = []
        mat = []
        for j in range(m):
            mat.append(valu)
            matrix.append(mat)
   # print(matrix)
    return matrix


rez1=get_matrix(2, 2, 10)
rez2=get_matrix(3, 5, 42)
rez3=get_matrix(4, 2, 13)
print(rez1)
print(rez2)
print(rez3)
