def flippingMatrix(matrix):
    matrix2 = matrix.copy()
    length = len(matrix)
    
    # for i in range(0, 2):
    #     if((matrix[i][0] + matrix[i][1]) < (matrix[i][2] + matrix[i][3])):
    #         matrix[i][0] = matrix2[i][3]
    #         matrix[i][1] = matrix2[i][2]
    #         matrix[i][2] = matrix2[i][1]
    #         matrix[i][3] = matrix2[i][0]
            
    #     matrix2 = matrix

    matrix[0][0] = matrix2[0][1]
    matrix[0][1] = matrix2[0][0]

    return matrix2

arr1 = [[1, 2], [3, 4]]
print(flippingMatrix(arr1))