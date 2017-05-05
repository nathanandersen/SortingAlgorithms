# A testing suite for sorts.
import random
from timeit import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def test(sort):
    wrapped = wrapper(test_inverted,sort)
    t = timeit(wrapped,number=1)
    result = 'Tested "{1}". Test took {0:.5f} seconds.'
    print(result.format(t,str(sort.__name__)))
    # how can we do assertion statements here
    # to truly test and debug?

def test_inverted(sort,k=1000):
    nums = [n for n in range(k)]
    random.shuffle(nums)
#    print(nums)
#    print("sorting")
    nums = sort(nums,lambda x:-x)
#    print(nums)
