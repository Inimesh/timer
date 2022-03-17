def gridTraversal(rows, cols, memo=None):
  memo = {} if memo == None else memo

  if rows == 0 or cols == 0: return 0
  if rows == 1 and cols == 1: return 1 

  key = (rows, cols)

  if key in memo:
    return memo[key]
  if key[::-1] in memo:
    return memo[key[::-1]]

  memo[key] = gridTraversal(rows-1, cols, memo) + gridTraversal(rows, cols-1, memo)
  return memo[key]


if __name__ == "__main__":
  print(gridTraversal(18,18))