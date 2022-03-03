import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

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

  X_Y_Spline = make_interp_spline(x_data, y_data)

  X_ = np.linspace(x_data.min(), x_data.max(), 8)
  Y_ = X_Y_Spline(X_)

  # x_data is input size, y_data is time in seconds
  # a, b = np.polyfit(x_data, y_data, 1)

  # plt.plot(x_data, y_data)
  # plt.plot(x_dat-a, a*x_data+b, color='purple', linewidth=2)

  plt.plot(X_, Y_)
  plt.scatter(x_data, y_data, s=1)

  plt.xlabel('Input size')
  plt.ylabel('Time (seconds)')
  plt.title('Algorithm Runtime vs. Input size')

  plt.show()