
def nthFibonacci(n):
  if n < 2:
    return 1

  return nthFibonacci(n-1) + nthFibonacci(n-2)


if __name__ == "__main__":
  for n in range(10):
    print(nthFibonacci(n))