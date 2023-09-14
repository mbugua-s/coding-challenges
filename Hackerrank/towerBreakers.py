def towerBreakers(n, m):
    allTowers = []
    emptyTowers = 0
    nonEmptyTowers = m
    fullTowers = m
    turn = 1

    for i in range(0, n):
        allTowers.append(m)

    while(emptyTowers < m):
