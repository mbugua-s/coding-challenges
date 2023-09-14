def diagonalDifference(arr):
    length = len(arr)
    diagonal1, diagonal2 = 0, 0

    for index in range(0, length):
        diagonal1 += arr[index][index]
        diagonal2 += arr[index][(length - 1) - index]

    difference = diagonal1 - diagonal2
    return(abs(difference))

arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
print(diagonalDifference(arr1))