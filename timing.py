from time import perf_counter_ns, process_time

def timer(callback, input):
  """
  args: algorithm (function), input
  returns: time in seconds (float)
  """

  # start = process_time()
  start = perf_counter_ns()
  callback(input)
  # end = process_time()
  end = perf_counter_ns()

  return (end - start)*(10**9)