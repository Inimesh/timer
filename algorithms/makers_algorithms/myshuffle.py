from time import time

def my_shuffle(arr):
  rand_num = lambda time_ms: eval(str(time_ms)[-2]) % len(arr)
  for i in range(len(arr)):
    rand_1 = rand_num(time())
    rand_2 = rand_num(time())

    arr[rand_1], arr[rand_2] = arr[rand_2], arr[rand_1]
  return arr


if __name__ == "__main__":
  arr = list(range(10))
  print(arr)
  print(my_shuffle(arr))
  print(my_shuffle(arr))
  print(my_shuffle(arr))
  print(my_shuffle(arr))
  print(my_shuffle(arr))
  print(my_shuffle(arr))