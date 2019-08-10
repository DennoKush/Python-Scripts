# Write a for loop that iterates over the names list to create a usernames list. 
# To create a username for each name, make everything lowercase and replace spaces with underscores

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    name = name.replace(" ","_").lower()
    usernames.append(name)
print(usernames)

# Create Usernames
# Write a for loop that iterates over the names list to create a usernames list. 
# To create a username for each name, make everything lowercase and replace spaces with underscores
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ","_"))

print(usernames)

# Modify Usernames with Range
# Write a for loop that uses range() to iterate over the positions in usernames to modify the list. 
# Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ","_")

print(usernames)
# Tag Counter
# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. 
# XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left 
# angle bracket "<" and ends with a right angle bracket ">"
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == "<" and token[-1] == ">":
        count += 1

print(count)
# Create an HTML List
# Write some code, including a for loop, that iterates over a list of strings and creates a single string, 
# html_str, which is an HTML list
items = ['first string', 'second string']
html_str = "<ul>\n"

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)