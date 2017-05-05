# A randomized QuickSort algorithm.
from random import randint
import Testing

def randQS(xs,key):
    if key is None:
        key = lambda x:x
    if len(xs) < 2:
        return xs
    else:
        partition = xs[randint(0,len(xs)-1)]
        l = []
        r = []
        matches = []
        for x in xs:
            if key(x) < key(partition):
                l.append(x)
            elif x is partition:
                matches.append(x)
            else:
                r.append(x)
        return randQS(l,key) + matches + randQS(r,key)

if __name__ == "__main__":
    Testing.test(randQS)
