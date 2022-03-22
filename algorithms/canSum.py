count = 0
def canSum(target, arr):
  global count
  count += 1
  print(count)
  if target == 0: return True
  if target < 0: return False

  for num in arr:
    remainder = target - num
    if canSum(remainder, arr): return True
  
  return False

print(canSum(7, [2, 3])) # True
print(canSum(7, [5, 3, 4, 7])) # True
print(canSum(7, [2, 4])) # False
print(canSum(8, [2, 3, 5])) # True
print(300**3)