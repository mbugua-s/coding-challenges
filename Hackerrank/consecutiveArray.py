def solution(statues):
    statues.sort()
    addition = 0
    extra = 0
    
    for i in range(0, (len(statues) - 2)):
        if(statues[i+1] - statues[i] > 1):
                addition = statues[i]
                extra += addition
                                
    return extra