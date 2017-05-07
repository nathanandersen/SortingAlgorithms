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
    for x,y in zip(xs[:-1],xs[1:]):
        if x > y: return False
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
