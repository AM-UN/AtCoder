# 入力
N, K = map(int, input().split())
s = [int(input()) for i in range(N)]

# 数列に0が存在する場合
if 0 in s:
    print(N)
    exit()

r, ans, now = 0, 0, 1

# 尺取り法で連続する要素の積がK以下の最長の部分列を求める
for l in range(N):
    while r < N and now*s[r] <= K:
        now *= s[r]
        r += 1
        ans = max(ans, r-l)
    if r == l:
        r += 1
    else:
        now //= s[l]
print(ans)

