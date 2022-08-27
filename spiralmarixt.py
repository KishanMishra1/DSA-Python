#Clockwise
def spiralOrder(matrix):
    return matrix and [*matrix.pop(0)]+ spiralOrder([*zip(*matrix)][::-1])
def display(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end=" ")
        print()
    print()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
display(matrix)
print(spiralOrder(matrix))

