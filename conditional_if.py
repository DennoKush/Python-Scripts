# First Example
phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

# Second Example
number = 119
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

# Third Example
age = 45

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay KES{} to ride the bus".format(age, ticket_price)
print(message)

# Using Truth Values of Objects
points = 100

# Set prize to default value of None
prize = None

# Use the value points to assign prize to the correct prize name
if points <= 50:
    prize = 'wooden rabbit'
elif 151 <= points <= 180:
    prize = 'wafer-thib mint'
elif points >= 181:
    prize = 'penguine'

# Use the truth value of prize to assign result to the correct message
if prize:
    result = 'Congratulations! You won a {}!'.format(prize)
else:
    result = 'Oh dear, no prize this time.'

print(result)