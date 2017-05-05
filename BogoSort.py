def bogosort(xs,key):
  while not is_in_order(xs):
    shuffle(xs)
   return xs
  
  
 def is_in_order(xs):
  for index,value in enumerate(xs):
    if not reduce(lambda x,y: x or y,map(lambda x: x < value, xs[index+1:])):
       return false
#    for val in xs[index+1:]:
 #     if value > val:
  #      return false
 return true
