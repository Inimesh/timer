from timing import timer

def collector(callback, input_set):
  """
  args: algorithm (function), set of inputs
  return: input size vs. runtime data (2D array)
  """
  data = []

  for input in input_set:
    datum = [len(input), timer(callback, input)]
    data.append(datum)

  return data

def collect_results_set(algo_callback, generator, inputs_per_test, test_runs=1):
  results_set = []
  for i in range(test_runs):
    set = generator(inputs_per_test)
    results = collector(algo_callback, set)
    results_set.append(results)

  return results_set

