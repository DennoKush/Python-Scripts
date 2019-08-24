# list comprehensions allows us to create a list using a for loop in one step
cities = ['nairobi, kenya', 'Daresalam, tanzania', 'mogadishu, somalia', 'kampala, uganda', 'kigali, rwanda']

capitalized_cities = [city.title() for city in cities]
print(capitalized_cities)

# You can also add conditionals to list comprehensions(listcomps). After the iterable, you can use the if keyword 
# to check a condition in each iteration

squares = [x**2 for x in range(9) if x%2==0]
print(squares)

# if you would like to add else, you have to move the conditionals to the beginning of the listcomp, 
# right after the expression 

squares = [x**2 if x%2==0 else x+3 for x in range(9)]
print(squares)

# use a list comprehension to create a list of names passed that only include those that scored at least 65

scores = {
            'Rick Sanchez':70,
            'Morty Smith':35,
            'Summer Smith':82,
            'Jerry Smith':23,
            'Beth Smith':98
}

passed = [name for name, score in scores.items() if score >= 65]
print(passed)