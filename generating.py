


import random


def generator():
  set = []

  for i in range(6):
    input = random.sample(range(100_000), 10**i)
    set.append(input)

  return set