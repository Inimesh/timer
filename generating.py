


import random


def generator(upper_bound):
  """
  returns: a 2D array of i lists of random integers between 0 - 99,999, 
  with lists making up set i containing i elements (i is range 9 - 29,999 in steps of 10),
  """
  set = []

  for i in range(9, upper_bound, 10):
    input = random.sample(range(100_000), i)
    set.append(input)

  return set