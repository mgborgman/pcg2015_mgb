import math

loose_change = [
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
]
# How many stacks of N units can we make for each denomination of coin?

coins = []
for coin in loose_change:
    coins.append(coin['denomination'])
    print coins

num_of_nickels = 0
num_of_dimes = 0
num_of_quarters = 0

for coin in coins:
    if coin == 'nickel':
        num_of_nickels += 1
    elif coin == 'dime':
        num_of_dimes += 1
    else:
        num_of_quarters += 1

stacks_of_nickels = math.ceil(num_of_nickels / 4.0)
stacks_of_dimes = math.ceil(num_of_dimes / 4.0)
stacks_of_quarters = math.ceil(num_of_quarters / 4.0)

print("num of nickels = " + str(num_of_nickels))
print("num of dimes = " + str(num_of_dimes))
print("num of quarters = " + str(num_of_quarters))
print("stacks of nickels = " + str(stacks_of_nickels))
print("stacks of dimes = " + str(stacks_of_dimes))
print("stacks of quarters = " + str(stacks_of_quarters))