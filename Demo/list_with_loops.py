animals = ['dog', 'mouse', 'cat', 'horse', 'octopus']

print(len(animals))
print(animals[0])

i = 0

while i < len(animals):
    print(animals[i])
    i += 1


"""
for every animal in the list called animals:
    print the animal


for every animal, a, in animals:
    print(a)
"""

for a in animals:
    print(a)


# print animals with three letters
for a in animals:
    if len(a) == 3:
        print(a)


# count animals with three letters
count = 0
for a in animals:
    if len(a) == 3:
        count += 1
print(count)
   
# count animals without three letters
count = 0
for a in animals:
    if len(a) != 3:
        count += 1
print(count)
