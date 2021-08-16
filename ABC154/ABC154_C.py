N = int(input())
A = list(map(int, input().split()))

# Aの中で被った数がなければYES、あればNOを出力
if len(A) == len(set(A)):
  print("YES")
else:
  print("NO")