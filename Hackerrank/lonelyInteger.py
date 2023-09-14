def lonelyinteger(a):
    a.sort()

    if len(a) == 1:
        return a[0]

    for index, number in enumerate(a):
        if index == 0:
            if a[index] != a[index + 1]:
                return a[index]
            
        elif index == (len(a)) - 1:
            if a[index] != a[index - 1]:
                return a[index]
            
        else:
            if a[index] != a[index - 1] and a[index] != a[index + 1]:
                return a[index]
        
a = [1, 2, 3, 2, 3, 1, 4]
print(lonelyinteger(a))