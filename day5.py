input = open("input/day5.txt", "r").read().split('\n\n')
inputStacks = input[0].split('\n')

numBoxes = inputStacks[-2].count('[')

stacks = [[] for _ in range(numBoxes)]

for row in inputStacks:
    for i in range(1,(3*numBoxes)+numBoxes-1,4):
        stacks[int(inputStacks[-1][i])-1].append(row[i])
        
stacks = [[j for j in i[:-1] if j!=' '] for i in stacks]

moves = input[1].split('\n')
moves = [[i for i in m.split(' ') if i.isdigit()] for m in moves]
moves = [{'amount': int(m[0]), 'oldStack':  int(m[1])-1, 'newStack': int(m[2])-1} for m in moves]

print(moves)

for m in moves:
    for _ in range(m['amount']):
        stacks[m['newStack']].insert(0,stacks[m['oldStack']].pop(0))   

print([s[0] for s in stacks])