N = int(input())
A = list(map(int, input().split()))

ans = [0] * N

# 何人直属の部下がいるか記録
for i in A:
  ans[i-1] += 1

# 改行区切りでそれぞれの社員が抱える直属の部下の人数を出力
print(*ans, sep="\n")