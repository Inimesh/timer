from time import process_time

def timer(algo):

  start = process_time()
  algo()
  end = process_time()

  return end - start