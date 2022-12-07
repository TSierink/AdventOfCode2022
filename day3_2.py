bags = open("input/day3.txt", "r").read().split("\n")

triplets = []
for i in range(0, len(bags), 3):
    triplets.append([bags[i], bags[i + 1], bags[i + 2]])

badges = [set(t[0]) & set(t[1]) & set(t[2]) for t in triplets]

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

badges = [priority.index(''.join(letter))+1 for letter in badges]

print(sum(badges))
