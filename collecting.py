from timing import timer


def collector(algo, input_set):
  """
  args: algorithm (function), set of inputs
  return: input size vs. runtime data (2D array)
  """
  data = []

  for input in input_set:
    datum = [input.length(), timer(algo, input)]
    data.append(datum)

  return data
