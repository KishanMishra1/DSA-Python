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

def display(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end=" ")
        print()
    print()

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
display(matrix)
clockwise_rotate(matrix,90)
display(matrix)

