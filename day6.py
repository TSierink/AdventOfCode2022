input = open("input/day6.txt", "r").read()

for i in range(len(input)-3):
    if len(set(input[i:i+4])) == 4:
        print(i+4)
        break