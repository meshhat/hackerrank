x = int(raw_input())
y = int(raw_input())
c = int(raw_input())
n = int(raw_input())
list = [[A, B, C] for A in range(x+1) for B in range(y+1) for C in range(z+1) if A+B+C != n]
print(list)
