def countingSort(arr):
    frequency = []
    counter = 0

    for i in range(0, 100):
        for j in arr:
            if i == j:
                counter += 1
        
        frequency.append(counter)
        counter = 0

    return frequency

arr1 = [1, 1, 2, 3, 5, 5]
print(countingSort(arr1))