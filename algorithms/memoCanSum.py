def memoCanSum(target, arr, memo=None):
  memo = {} if memo == None else memo
  if target in memo: return memo[target]
  if target == 0: return True
  if target < 0: return False
  
  for num in arr:
    remainder = target - num
    memo[remainder] = memoCanSum(remainder, arr, memo)
    if memo[remainder]: return True

  memo[target] = False
  return False

print(memoCanSum(7, [2, 3])) # True
print(memoCanSum(7, [5, 3, 4, 7])) # True
print(memoCanSum(7, [2, 4])) # False
print(memoCanSum(8, [2, 3, 5])) # True
print(memoCanSum(300, [7, 14])) # False