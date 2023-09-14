def matchingStrings(strings, queries):
    occurences = []

    for query in queries:
        count = 0

        for str in strings:
            if query == str:
                count += 1
        
        occurences.append(count)

    #print(occurences)
    return occurences

matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc'])
