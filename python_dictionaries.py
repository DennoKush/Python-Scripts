# Using a for loop to create a set of counters
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
#print(word_counter)

# Using the get method
word_counter = {}

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1

#print(word_counter)

# Iterating through Dictionaries with For Loops
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
# Iterating through it the usual way with a for loop will return the keys
for key in cast:
    print(key)
print()
# If you wish to iterate through both keys and values, you can use the 
# built-in method items
for key, value in cast.items():
    print("Actor: {}  Role{}".format(key, value))

# Fruit Basket 1

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit in basket_items:
#if the key is in the list of fruits, add the value (number of fruits) to result
    if fruit in fruits:
        result += basket_items[fruit]

print(result)

# Fruit Basket 2

#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for fruit in basket_items:
    if fruit in fruits:
        result += basket_items[fruit]
print(result)

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for fruit in basket_items:
    if fruit in fruits:
        result += basket_items[fruit]
print(result)


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for fruit in basket_items:
    if fruit in fruits:
        result += basket_items[fruit]
print(result)


# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit in basket_items:
#if the key is in the list of fruits, add to fruit_count.
    if fruit in fruits:
        fruit_count += basket_items[fruit]
#if the key is not in the list, then add to the not_fruit_count
    else:
        not_fruit_count += basket_items[fruit]

print(fruit_count, not_fruit_count)