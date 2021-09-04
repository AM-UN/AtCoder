N = int(input())

# 文字列Sの出現回数を記録
d = {}
for _ in range(N):
    S = input()
    if S in d:
        d[S] += 1
    else:
        d[S] = 1

# 出現回数が最も多かった文字列を辞書順に出力
ans = []
max_j = max(d.values())
for i, j in d.items():
  if j == max_j:
    ans.append(i)
ans.sort()

print(*ans, sep='\n')