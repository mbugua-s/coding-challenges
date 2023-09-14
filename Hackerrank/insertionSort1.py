def insertionSort1(n, arr):
    value_sorted = arr[n - 1]
    for x in range(n - 1, -1, -1):
        if(x == 0 and arr[x] > value_sorted):
            arr[x + 1] = arr[x]
            arr[x] = value_sorted
            for x in arr:
                print(x, end = " ")
            break

        if(arr[x - 1] >= value_sorted):
            arr[x] = arr[x - 1]

            for x in arr:
                print(x, end = " ")
            print("")

        else:
            arr[x] = value_sorted
            for x in arr:
                print(x, end = " ")
            break
        
    # Copy left, update current (doesn't meet all test cases)
    """ arr[n - 1] = arr[n - 2]
    for x in range(n - 2, -1, -1):
        if(x == 0 and arr[x] > value_sorted):
            arr[x + 1] = arr[x]
            arr[x] = value_sorted
            for x in arr:
                print(x, end = " ")
            break

        if(arr[x] >= value_sorted):
            arr[x + 1] = arr[x]

            for x in arr:
                print(x, end = " ")
            print("")

        else:
            arr[x + 1] = value_sorted
            for x in arr:
                print(x, end = " ")
            break """

# arr = [2, 4, 6, 8, 3]
# insertionSort1(5, arr)
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
insertionSort1(10, arr)