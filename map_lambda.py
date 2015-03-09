x = int(raw_input())
def fib(n):
  a = 0
  b = 1
  for i in range(0, n):
    temp = a
    a = b
    b = temp + b
  return a

lis = []
for c in range(0, x):
  lis.append(fib(c))

g = lambda x: x** 3
print(list(map(g, lis)))
