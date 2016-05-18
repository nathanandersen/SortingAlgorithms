# A testing suite for sorts.
import random


def test(sort):
    test_inverted(sort)
    # how can we do assertion statements here
    # to truly test and debug?
    
def test_inverted(sort):
    nums = [n for n in range(1000)]
    random.shuffle(nums)
    print(nums)
    print("sorting")
    nums = sort(nums,lambda x:-x)
    print(nums)
