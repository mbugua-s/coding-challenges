def solution(sequence):
    increasing = 0
    oneLess = []
    # max = sequence[0]
    
    # Brute Force Method

    sortedSequence = sorted(sequence)

    for i in range(0, len(sequence)):
        increasing = False
        oneLess = sequence[:]
        del oneLess[i]

        oneLessSorted = sorted(oneLess)
        oneLessSortedSet = sorted(list(set(oneLess)))

        if(oneLess != oneLessSorted or oneLess != oneLessSortedSet):
            increasing = False
        
        else:
            increasing = True
            break
        
        # for i in range(0, len(oneLess) - 1):
        #     if oneLess[i] >= oneLess[i + 1]:
        #         sorted = False
        #         break
                
        # if increasing == True:
        #     break
           
    return increasing

print(solution([123, -17, -5, 1, 2, 3, 12, 43, 45]))


    # for i in range(1, len(sequence)):
    #     if(sequence[i] <= max):
    #         increasing += 1
    #         print("max", max)
    #         print("inc", increasing)
            
    #     else:
    #         max = sequence[i]
    #         print("max", max)
    #         print("inc", increasing)
    
    # for i in range(1, len(sequence)):
    #     if(sequence[i] >= sequence[i + 1] or sequence[i] <= max):
    #         increasing += 1
            # print("max", max)
            # print("inc", increasing)
            
        # else:
        #     max = sequence[i]
            # print("max", max)
            # print("inc", increasing)

    # for i in range(0, len(sequence) - 1):
    #     if(sequence[i] >= sequence[i + 1]):
    #         increasing += 1
            
    # if(increasing > 0):
    #     return False
    
    # else:
    #     return True
