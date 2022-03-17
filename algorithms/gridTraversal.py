def gridTraversal(rows, cols):
  if rows == 0 or cols == 0: return 0
  if rows == 1 and cols == 1: return 1 

  return gridTraversal(rows-1, cols) + gridTraversal(rows, cols-1)


if __name__ == "__main__":
  for i in range (14):
    print(gridTraversal(i,i))