def howSum(target, arr):
  if target == 0: return []
  if target < 0: return None

  for num in arr:
    remainder = target - num
    next = howSum(remainder, arr)
    if next != None: return [*next, num]

  return None


print(howSum(7, [2, 3])) ## [3, 2, 2]
print(howSum(7, [5, 3, 4, 7])) ## [4, 3]
print(howSum(7, [2, 4])) ## null
print(howSum(8, [2, 3, 5])) ## [2, 2, 2, 2]
print(howSum(8, [3, 5, 2])) ## [2, 3, 3]
print(howSum(100, [7, 14])) ## null