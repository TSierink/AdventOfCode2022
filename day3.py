priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

bags = open("input/day3.txt", "r").read().split('\n')
bags = [set(l[:(len(l)//2)])&set(l[(len(l)//2):]) for l in bags] 
bags = [priority.index(''.join(letter))+1 for letter in bags]

print(sum(bags))