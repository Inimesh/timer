def gridTraversal(rows, cols):
  '''A function that determines the number of unique paths that can be taken
  to a target position. Provided you can only move in two directions'''
  if rows == 0 or cols == 0: return 0
  if rows == 1 and cols == 1: return 1 

  return gridTraversal(rows-1, cols) + gridTraversal(rows, cols-1)


if __name__ == "__main__":
  for i in range (14):
    print(gridTraversal(i,i))