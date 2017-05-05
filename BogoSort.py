def bogosort(xs,key):
  while not is_in_order(xs):
    shuffle(xs)
   return xs
  
  
 def is_in_order(xs):
  for index,value in enumerate(xs):
    for val in xs[index+1:]:
      if value > val:
        return false
 return true
