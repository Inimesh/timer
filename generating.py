


import random


def generator():
  """
  returns: a 2D array of n lists of random integers between 0 - 99,999, 
  with each list containing 10**n elements (n is a range 0-5)
  """
  set = []

  for i in range(6):
    input = random.sample(range(100_000), 10**i)
    set.append(input)

  return set