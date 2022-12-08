ranges = open("input/day4.txt", "r").read()
ranges = [[[int(r) for r in range2.split('-')] for range2 in range1.split(',')] for range1 in ranges.split('\n')]
ranges = [[range(r[0],r[1]+1) for r in range1] for range1 in ranges]

bools = [(set(r[0]).issubset(set(r[1])) or set(r[1]).issubset(set(r[0]))) for r in ranges]

print(bools.count(True))