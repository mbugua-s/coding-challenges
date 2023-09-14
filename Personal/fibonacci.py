def fibonacci(n, numbers, start = 0, end = 1):
    if(len(numbers) == 0):
        numbers.append(start)
        numbers.append(end)
        return fibonacci(n - 1, numbers, start, end)

    elif(n > 1):
        numbers.append(start + end)
        return fibonacci(n - 1, numbers, end, start + end)
    
    else:
        return numbers
    
arr1 = []
print(fibonacci(5, arr1))
