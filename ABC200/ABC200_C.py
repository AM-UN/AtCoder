N = int(input())
A = list(map(int, input().split()))

remainder = [0 for i in range(200)]
ans = 0

for i in A:
  remainder[i % 200] += 1

for i in range(200):
  ans += (remainder[i] * (remainder[i]-1)) // 2

print(ans)