# shuffle cards:
# take a deck of n cards, labelled 1 -> n
# take an int m for how many times we shuffle
# take m ints, ki, everytime we shuffle we take the top ki cards, put it at the
# the bottom and then print the top card

# Shopee interview problem
# The trick is that when you shuffle like this you don't change the order of
# the deck, so you can just skip the shuffle

n,m = list(map(int,input().strip().split(' ')))
ch = list(map(int,input().strip().split(' ')))

N = [i+1 for i in range(n)]

cur = 0
for c in ch:
    cur += c
    cur %= len(N)
    print(N.pop(cur))

# god i hate technical interviews
