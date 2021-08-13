N = int(input())
A = [int(input()) for i in range(N)]

# Aの数列のうち、Aiをのぞいた最大値を出力
B = sorted(A, reverse=True)
for i in A:
  if i != B[0]:
    print(B[0])
  else:
    print(B[1])