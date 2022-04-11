import sys

def fibonacci(current, previous, sum_):
  if current == 1:
    return fibonacci(2,1,0)
  if current == 2:
    return fibonacci(3,2,2)
  if current > 4000000:
    return sum_
  if(current % 2 == 0):
    sum_ += current
    return fibonacci(current + previous, current, sum_)
  else:
    return fibonacci(current + previous, current, sum_)

def main():
    print("starting fibonacci...")
    s = fibonacci(1,2,0)
    print(s)
      
if __name__ == '__main__':
  main()
