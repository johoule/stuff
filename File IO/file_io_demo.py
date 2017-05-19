# open a file
file = open('last_words.txt', 'r')
print(file)
print()

# read individual lines
line1 = file.readline()
line2 = file.readline()
print(line1)
print(line2)
print()

# read the entire file file
contents = file.read()
print(contents)
print()

# close the file
file.close()


# read files into a list
file2 = open('movies.txt', 'r')
movies = file2.readlines()
print(movies)
print()
file2.close()

# using 'with' automatically closes when finished
# splitlines() separates on linebreak and removes
# the newline character
with open('movies.txt', 'r') as f:
    movies = f.read().splitlines()
    
print(movies)
print()


# write a file
# try changeing 'w' to 'a' and see what happens
# (You'll need to run the program more than once)
file3 = open('new_file.txt', 'w')
file3.write('This is one line.')
file3.write('This is another.\n')
file3.write('This is actually on the next line')
file3.close()


with open('scrabble_list.txt') as f:
    words = f.read().splitlines()
    
print(words[:10])

import random
print(random.choice(words))

# use a for loop to process the list
''' how many words end with an s? '''
count = 0
for w in words:
    if w[-1] == 's':
        count += 1

print(count)

''' how many words are 2 letters long?'''
count = 0
for w in words:
    if len(w) == 2:
        count += 1

print(count)

''' make a new file with all words that are 2 letters long '''

with open('two_letters.txt', 'w') as f:
    for w in words:
        if len(w) == 2
            f.write(w + "\n")
