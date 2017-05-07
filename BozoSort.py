from random import sample

def bozosort(xs,key=None):
    if key is None:
        key = lambda x:x
    indices = list(range(len(xs)))
    while not is_in_order(xs,key):
        a,b = sample(indices,2)
        xs[a],xs[b] = xs[b],xs[a]
    return xs


def is_in_order(xs,key):
    for x,y in zip(xs[:-1],xs[1:]):
        if x > y: return False
    return True


from Testing import test_inverted
from Testing import wrapper

def special_test(n):
    test_inverted(bozosort,n)


if __name__ == "__main__":
    from timeit import timeit
    for n in range(2,11):
        t = timeit(wrapper(special_test,n),number=1)
        print('N: {0} - Time: {1:.5f} seconds'.format(n,t))
