# A randomized QuickSort algorithm.
import random
import Testing

def randQS(xs,key):
    if key is None:
        key = lambda x:x
    if len(xs) < 2:
        return xs
    else:
        partition = xs[random.randint(0,len(xs)-1)]
        l = []
        r = []
        matches = []
        for x in xs:
            if key(x) < key(partition):
                l.append(x)
            elif x is not partition:
                r.append(x)
            else:
                matches.append(x)
        return randQS(l,key) + matches + randQS(r,key)


if __name__ == "__main__":
    Testing.test(randQS)
