from jinja2 import Undefined


def memoNthFibonacci(n, memo=None):
  if memo == None:
    memo = {}

  if n < 2:
    return 1

  if n not in memo:
    memo[n] = memoNthFibonacci(n-1, memo) + memoNthFibonacci(n-2, memo)

  return memo[n]

if __name__ == "__main__":
  for n in range(50):
    print(memoNthFibonacci(n))