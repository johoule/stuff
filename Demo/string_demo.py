pangram = "The quick brown fox jumps over the lazy dog."

print(pangram)

# find the length of a string
num_chars = len(pangram)
print(num_chars)

# select individual characters from a string
first = pangram[0]
twelve = pangram[12]
last = pangram[num_chars - 1]
also_last = pangram[-1]

print(first, twelve, last, also_last)

# what if we try to look outside of the range?
# uncomment lines below to test
#print( pangram[-4] )
#print( pangram[50] )

# get a "slice" of a string
print( pangram[4:12] )
print( pangram[0:12] )
print( pangram[:12] )
print( pangram[12:] )
print( pangram[12:-1] )
print( pangram[12:len(pangram)] )

# get the index of a string within a string
print(pangram.find('q'))
print(pangram.find('T'))
print(pangram.find('fox'))
print(pangram.find('B'))
