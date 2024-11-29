import random

# "randrom.choice" we can use this choose between some given or provided data for example: 
# random.choice(["heads","tails"]) it will choose from one of these and will return that particular value.

# "random.randint" we can use this randomly choose any integer from the provided range. For Example:
# random.randint(a,b) given example shows "a" starting range and "b" an ending range to randomly choose an integer

# below is the given example random.shuffle which shuffle the provided list of items.
cards = ["jack", "queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)