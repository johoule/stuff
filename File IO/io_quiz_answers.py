# Comuter Programming 1
# File IO Quiz
#
# Names: Jordan Houle

# Answers to 1 - 11
'''

1) d               2) a               3) b. r | c. r+

4) a, c, d         5) b               6) b, c,

7) c               8) d               9) b

10) c              11) a

'''


#12
file = open('scrabble_list.txt', 'r')
words = file.readlines()


#13
print(len(words))


#14

with open('scrabble_list.txt') as f:
    words = f.read().splitlines()

print(words[:10])


#15
count = len(words)
for w in words:
    if 'e' in w:
        count -= 1

print(count)


#16
with open('same_letters.txt', 'w') as f:
    for w in words:
        if w[0] == w[-1]:
            f.write(w + "\n")
