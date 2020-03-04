import collections
a = [2,3,4,5,6,8,7,6,5,18]

def cost(size,m):
    pair = collections.Counter(a)
    money = 0
    if pair[size] >= 1:
        pair[size] = pair[size] - 1
        money += m
    print pair
    print money

cost(6,50)
cost(6,40)