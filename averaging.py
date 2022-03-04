def mean_average(*args):
  """
  input: an unspecified amount of 2D arrays containing x (input size) and y (time) values for plot.
  returns: a single 2D array with identical x values, and mean averaged y values
  """
  zipped_results = list(zip(*args))

  answer = []
  for group in zipped_results:
    point = [sum(l)/len(l) for l in zip(*group)]
    point[0] = int(point[0])

    answer.append(point)

  return answer