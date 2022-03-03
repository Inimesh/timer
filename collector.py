from timing import timer


def collector(algo, input_set):
  data = []

  for input in input_set:
    datum = [input.length(), timer(algo(input))]
    data.append(datum)

  return data
