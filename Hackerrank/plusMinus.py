myarray = [-6, -8, 0, 0, 5, 9, 10,1, 1, 0, -1, -1, 100]
def plusMinus(arr):
    if len(arr) > 0 and len(arr) <= 100:
        positive = 0
        negative = 0
        zero = 0
        valid = True
        for num in arr:
            if num > 100 or num < -100:
                valid = False
                break

        if valid:
            for num in arr:
                if num > 0:
                    positive += 1
                elif num == 0:
                    zero +=1
                else:
                    negative += 1
        
            print("{:.6f}".format(positive/len(arr)))
            print("{:.6f}".format(negative/len(arr)))
            print("{:.6f}".format(zero/len(arr)))


plusMinus(myarray)
