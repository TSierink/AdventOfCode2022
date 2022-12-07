lossScore = 0
drawScore = 3
winScore = 6

RockScore = 1
PaperScore = 2
ScissorScore = 3

moveDict = {
    "A": ("Rock",RockScore),
    "X": ("Rock",RockScore),
    "B": ("Paper",PaperScore),
    "Y": ("Paper",PaperScore),
    "C": ("Scissors",ScissorScore),
    "Z": ("Scissors",ScissorScore)
}

resultDict = {
    ("Rock","Rock"): drawScore,
    ("Rock","Paper"): winScore,
    ("Rock","Scissors"): lossScore,
    ("Paper","Rock"): lossScore,
    ("Paper","Paper"): drawScore,
    ("Paper","Scissors"): winScore,
    ("Scissors","Rock"): winScore,
    ("Scissors","Paper"): lossScore,
    ("Scissors","Scissors"): drawScore   
}

moves = open("input/day2.txt", "r").read().split('\n')

result = 0
for m in moves:
    opp = moveDict[m[0]]
    you = moveDict[m[2]]
    result += resultDict[(opp[0],you[0])] + you[1]

print(result)