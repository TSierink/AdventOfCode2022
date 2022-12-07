f = open("input/day1.txt", "r").read().split('\n\n')
#DOESTHISWORK
f = [line.split('\n') for line in f]

f = [[int(n) for n in line] for line in f]

print(max([sum(line) for line in f]))
print(max(f))