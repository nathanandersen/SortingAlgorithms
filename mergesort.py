# A Merge-Sort implementation in Python
# (c) 2016 Nathan Andersen
import random

def mergeSort(xs,key=None):
    """Sorts a list, xs, in O(n*log n) time."""
    if key is None:
        key = lambda x:x
    if len(xs) < 2:
        return xs
    else:
        # sort the l and r halves
        mid = len(xs) // 2
        l = mergeSort(xs[:mid],key)
        r = mergeSort(xs[mid:],key)
        # merge them r together
        return merge(l,r,key)

def merge(l,r,key):
    """A merge routine to complete the mergesort."""
    result = []
    l_ptr = 0
    r_ptr = 0
    while (l_ptr < len(l) or r_ptr < len(r)):
        if l_ptr == len(l):
            # if we have added everything from the l
            result.extend(r[r_ptr:])
            return result
        elif r_ptr == len(r):
            # we have added everything from the r
            result.extend(l[l_ptr:])
            return result
        elif key(l[l_ptr]) < key(r[r_ptr]):
            result.append(l[l_ptr])
            l_ptr += 1
        else:
            result.append(r[r_ptr])
            r_ptr += 1


if __name__ == "__main__":
    nums = [n for n in range(1000)]
    random.shuffle(nums)
    print(nums)
    print("sorting")
    nums = mergeSort(nums,lambda x:(-1*x))
    print(nums)
