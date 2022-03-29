def memoNthFibonacci(n, memo=None):
  '''A memoized version of the nthFibonacci function'''
  if memo == None: memo = {}
  if n < 2: return 1

  if n in memo: 
    return memo[n]

  memo[n] = memoNthFibonacci(n-1, memo) + memoNthFibonacci(n-2, memo)
  return memo[n]

if __name__ == "__main__":
  for n in range(50):
    print(memoNthFibonacci(n))