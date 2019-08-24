manifest = [('bananas', 15), ('mattresses',24),('dog kennels',42),('machine', 120), ('cheese', 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print('METHOD 1')
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print('current weight: {}'.format(weight))
    if weight >= 100:
        print(' breaking loop now!')
        break
    else:
        print(' adding {} ({})'.format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print('\n Final Weight: {}'.format(weight))
print('Final items: {}'.format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print('current weight: {}'.format(weight))
    if weight >= 100:
        print(' breaking from the loop now!')
        break
    elif weight + cargo_weight > 100:
        print(' skipping {} ({})'.format(cargo_name, cargo_weight))
        continue
    else:
        print(' adding {} ({})'.format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print('\n Final weight: {}'.format(weight))
print('Final Items: {}'.format(items))


# write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long
# You should create the news ticker by adding headlines from the headlines list, inserting a space in between
# each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 
# characters long.

headlines = ['Local Bear Eaten by Man',
            'Legislature Announces New Laws',
            'Peasant Discovers Violence Inherent in System',
            'Cat Rescues Fireman Stuck in Tree',
            'Brave Knight Runs Away',
            'Papperbok Review: Totally Triffic']
news_ticker = ''
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)
print(len(news_ticker))