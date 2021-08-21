N = int(input())
P = list(map(int, input().split()))

minimum = P[0]
ans = 0

# i未満にP[i]より大きい値がなければカウント
for i in range(N):
  if P[i] <= minimum:
    ans += 1
    minimum = P[i]
print(ans)