N = int(input())
A = list(map(int, input().split()))

ans = [0] * N

for i in range(N):
  num = A[i]
  ans[num - 1] = i + 1 

print(*ans)