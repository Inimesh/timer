from time import process_time

def timer(algo, input):
  """
  args: algorithm (function), input
  returns: time in seconds (float)
  """

  start = process_time()
  algo(input)
  end = process_time()

  return end - start