import Testing

from functools import reduce
from random import shuffle

def bogosort(xs,key=None):
    if key is None:
        key = lambda x:x
    while not is_in_order(xs,key):
        shuffle(xs)
    return xs


def is_in_order(xs,key):
    for index,value in enumerate(xs[:-1]):
        if reduce(lambda x,y: x or y,map(lambda x: key(x) < key(value), xs[index+1:])):
            # because when you're killing an ant with a missile
            # go big or go home
            return False
#        for val in xs[index+1:]
#            if value > val:
#                return false
    return True


from Testing import test_inverted
from Testing import wrapper

def special_test(n):
    test_inverted(bogosort,n)


if __name__ == "__main__":
    from timeit import timeit
    for n in range(2,11):
        t = timeit(wrapper(special_test,n),number=1)
        print('N: {0} - Time: {1:.5f} seconds'.format(n,t))
