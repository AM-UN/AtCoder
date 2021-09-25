K, N = map(int, input().split())
A = list(map(int, input().split()))

ans = []

# Aのそれぞれの要素の差分を求め、ansに追加
for i in range(N-1):
  ans.append(A[i+1] - A[i])

# Aの初項と末尾の項のみを別にしてansに追加
ans.append(A[0] + (K - A[N-1]))

print(sum(ans) - max(ans))