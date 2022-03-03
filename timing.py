from time import process_time

def timer(callback, input):
  """
  args: algorithm (function), input
  returns: time in seconds (float)
  """

  start = process_time()
  callback(input)
  end = process_time()

  return end - start