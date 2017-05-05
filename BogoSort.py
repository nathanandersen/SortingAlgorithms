from functools import reduce

def bogosort(xs,key):
    while not is_in_order(xs):
        shuffle(xs)
    return xs


def is_in_order(xs):
    for index,value in enumerate(xs[:-1]):
        if reduce(lambda x,y: x or y,map(lambda x: x < value, xs[index+1:])):
            # because when you're killing an ant with a missile
            # go big or go home
            return False
#        for val in xs[index+1:]
#            if value > val:
#                return false
    return True
