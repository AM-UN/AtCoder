N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort(reverse = True)

# Hの中でK番目に大きい数より小さい数の総和を出力
ans = 0
for i in range(N):
  if K < i + 1:
    ans += H[i]
print(ans)