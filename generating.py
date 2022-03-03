import random


def generator_gran(upper_bound):
  """
  args: upper_bound (int)
  returns: a 2D array of i lists of random integers between 0 - upper_bound
  with lists making up set i containing i elements (i is range 9 - 29,999 in steps of 10),
  """
  set = []

  for i in range(9, upper_bound, 10):
    input = random.sample(range(100_000), i)
    set.append(input)

  return set

def generator_large(upper_bound):
  """
  args: upper_bound (int)
  returns: a 2D array of i range(1 - upperbound) lists of random integers between 0 - upper_bound*10**i
  """
  set = []

  for i in range(1, upper_bound):
    input = random.sample(range(upper_bound*10**i), 10**i)
    set.append(input)

  return set