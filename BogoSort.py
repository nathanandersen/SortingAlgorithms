from QuickSort import quickSort


def bogosort(xs,key):
  while not is_in_order(xs):
    shuffle(xs)
   return xs
  
  
 def is_in_order(xs):
    sorted = quickSort(xs)
    return sorted == xs
