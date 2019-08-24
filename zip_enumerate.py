# ZIP
# returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains 
# the elements in that position from all the iterables.

a, b = ['a','b','c'], [1,2,3]
c = list(zip(a, b))
print(c)

letters = ['a','b','c']
nums = [1,2,3]

for letter, num in zip(letters, nums):
    print('{}: {}'.format(letter, num))

# in addition to zipping two lists together, you can also unzip a list into tuples using asterisk

some_list = [('a',1), ('b',2), ('c', 3)]
letters, nums = zip(*some_list)
print(letters)
print(nums)

# ENUMERATE
# is a built in function that returns an iterator of tuples containing indices and values of a list.
# You'll often use this when you want the index along with each element of an iterable in a loop.

letters = ['a','b','c','d']
for i, letter in enumerate(letters):
    print(i, letter)

# use zip to transpose data from a 4-by-3 matrix to a -by-4 matrix.
data = ((0,1,2),(3,4,5),(6,7,8),(9,10,11))

data_transpose = tuple(zip(*data))
print(data_transpose)

# use enumerate to modify the cast list so that each element contains the name followed by the character's
# corresponding height. For example, the first element of cast should change from "Barney Stinson" to 
# "Barney Stinson 72"

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, name in enumerate(cast):
    cast[i] = name + " " + str(heights[i])

print(cast)