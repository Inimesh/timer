import matplotlib.pyplot as plt
import numpy as np

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

  x_data = np.array(x_data)
  y_data = np.array(y_data)

  # x_data is input size, y_data is time in seconds
  a, b = np.polyfit(x_data, y_data, 1)

  # plt.plot(x_data, y_data)
  plt.scatter(x_data, y_data)
  plt.plot(x_data, a*x_data+b)

  plt.xlabel('Input size')
  plt.ylabel('Time (seconds)')
  plt.title('Algorithm Runtime vs. Input size')

  plt.show()