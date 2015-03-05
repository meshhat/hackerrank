import fileinput
a,b = fileinput.input()

var=0
for i in range(len(a)):
  if a[i:i+len(b)]==b:
    var += 1
print(var)
