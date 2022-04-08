def howSum(target, arr, memo=None):
  '''A memoized version of the howSum function'''
  memo = {} if memo == None else memo
  if target in memo: return memo[target]
  if target == 0: return []
  if target < 0: return None

  for num in arr:
    remainder = target - num
    next = howSum(remainder, arr, memo)
    if next != None: 
      memo[target] = [*next, num]
      return memo[target]

  memo[target] = None
  return None


print(howSum(7, [2, 3])) ## [3, 2, 2]
print(howSum(7, [5, 3, 4, 7])) ## [4, 3]
print(howSum(7, [2, 4])) ## null
print(howSum(8, [2, 3, 5])) ## [2, 2, 2, 2]
print(howSum(8, [3, 5, 2])) ## [2, 3, 3]
print(howSum(300, [7, 14])) ## null