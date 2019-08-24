# Factorials with While Loops

# number to find the factorial of
number = 5
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)

# Factorials with For Loops

# number we'll find the factorials of
number = 6
# start with our product equal to one
product = 1
# calculate factorial of number with a for loop
for num in range(2, number +1):
    product *= num

# print the factorial of number
print(product)