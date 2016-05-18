# A standard quicksort

import Testing

def quickSort(xs,key):
    if key is None:
        key = lambda x:x
    if len(xs) < 2:
        return xs
    else:
        partition = xs[0]
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
        return quickSort(l,key) + matches + quickSort(r,key)
    
if __name__ == "__main__":
    Testing.test(quickSort)
