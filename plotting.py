import matplotlib.pyplot as plt

def plotter(data):
  """
  args: 2D array of time vs input_size data
  return: plot a cartesian graph of the data
  """
  x_data = []
  y_data = []

  for datum in data:
    x_data.append(datum[0])
    y_data.append(datum[1])

  # x_data is input size, y_data is time in seconds
  plt.plot(x_data, y_data)
  plt.xlabel('Input size')
  plt.ylabel('Time (seconds)')
  plt.title('Algorithm Runtime vs. Input size')

  plt.show()

  return True


plotter([ [5, 2], [6, 4], [7, 5], [8, 5.5] ])

