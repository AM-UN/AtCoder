N = int(input())
X = list(map(int, input().split()))

ans = float('INF')
for i in range(1, 101):
  sum = 0
  for j in X:
    sum += (j - i) ** 2
  ans = min(ans, sum)

print(ans)