# Timing framework

## Description

This is a simple timing framework written in Python to deduce the time complexity of algorithms.

## Screenshots

using ipython Jupyter notebooks to interactively use program and visualize data:

![screenshot_2](https://user-images.githubusercontent.com/72313368/156797166-b5341f1d-67e2-4da9-8662-9fad2a578bfb.png)

## Dependencies
Python3 Pacakges:
- numpy
- matplotlib


## Usage

You can use a REPL for to run the program but it is advised to use jupyter notebooks online.

> Alternatively you can install the VS code extensions "Jupyter" and "Jupyter Notebook Renderers", say yes to installing required dependencies, then using the interactive page to run the code as seen in the screenshot.

A useful library of sorting algorithms 'pysort' can be got via 

```bash
pip3 install pysort
```

1. Define a function that is to be used as a callback, and call your algorithm inside the body of this function using the args supplied to the callback

```python
def algo_callback(arg):
  your_algorithm(arg)
```

2. Pass this callback along with the desired generator (see below for generator options), number of inputs per test, and the number of test runs (default value is 1). The below example is using the generator type `generator_gran`, 2500 inputs, and a results sample size of 20

```python
results_set = collect_results_set(algo_callback, generator_type, 2500, 20)
```

3. To acquire a mean average or our results, pass the unpacked (* operator) results set to the mean_average function

```python
mean_average_results = mean_average(*results_set)
```

4. Then plot your averaged data using the plotter function. This plotter plots a scatter graph of input size vs. time (seconds) overlain with a curved line of best fit using the numpy library's `polyfit` function, using a cubic degree.

```python
plotter(mean_average_results)
```
