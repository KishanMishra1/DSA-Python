#Clockwise
def clockwise_rotate(matrix,n):
    n=n//90
    while(n):
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()
        n-=1
    return matrix

def anticlock_rotate(matrix,n):
    n=n//90
    while(n):
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        matrix.reverse()
        n-=1
    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(anticlock_rotate(matrix,180))
