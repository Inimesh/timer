


import random


def generator():
  """
  returns: a 2D array of i lists of random integers between 0 - 99,999, 
  with lists making up set i containing i elements (i is range 9 - 29,999 in steps of 10),
  """
  set = []

  for i in range(9, 30_000, 10):
    input = random.sample(range(100_000), i)
    set.append(input)

  # for i in range(3, 6):
  #   input = random.sample(range(100_000), 10**i)
  #   set.append(input)

  # set.append(random.sample(range(100_000), 100_000))

  return set