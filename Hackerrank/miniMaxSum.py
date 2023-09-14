def miniMaxSum(arr):
    arr.sort()
    length = len(arr)
    minSum, maxSum = 0, 0

    for index, element in enumerate(arr):
        if(index < (length - 1)):
            minSum += element
        
        if(index > 0):
            maxSum += element

    print(minSum, maxSum)

arr1 = [1, 3, 5, 7, 9]
miniMaxSum(arr1)