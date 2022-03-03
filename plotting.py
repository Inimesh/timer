import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d

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

  z = np.polyfit(x_data, y_data, 3)
  f = np.poly1d(z)

  x_new = np.linspace(x_data[0], x_data[-1], 50)
  y_new= f(x_new)

  plt.scatter(x_data, y_data, s=1)
  plt.plot(x_new, y_new, color='purple', linewidth=1)
  # plt.xlim([x[0]-1, x[-1] + 1 ])
  plt.show()


  plt.xlabel('Input size')
  plt.ylabel('Time (seconds)')
  plt.title('Algorithm Runtime vs. Input size')

  # plt.show()