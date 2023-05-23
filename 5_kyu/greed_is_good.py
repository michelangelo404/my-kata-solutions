#Greed is good

def score(dice):
    val = [{3:1000, 1:100, 2:200, 4:1100,5:1200},
           {3:200, 4:200, 5:200},
           {3:300, 4:300, 5:300},
           {3:400, 4:400, 5:400},
           {3:500, 1:50, 2:100, 4:550, 5:600},
           {3:600}]
    points = 0
    for i in range(1,7):
        c = dice.count(i)
        if c in val[i-1]:
            points += val[i-1][c]
    return points