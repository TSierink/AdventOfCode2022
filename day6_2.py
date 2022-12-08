input = open("input/day6.txt", "r").read()

for i in range(len(input)-13):
    if len(set(input[i:i+14])) == 14:
        print(i+14)
        break