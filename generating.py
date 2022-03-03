


import random


def generator():
  """
  returns: a 2D array of i+n lists of random integers between 0 - 99,999, 
  with lists making up set i containing i elements (i is range 0 - 999),
  and lists making up set n containing 10**n elements (n is a range 0-5)
  """
  set = []

  for i in range(1, 1000):
    input = random.sample(range(100_000), i)
    set.append(input)

  for i in range(3, 6):
    input = random.sample(range(100_000), 10**i)
    set.append(input)

  return set