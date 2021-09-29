N, M = map(int, input().split())

# リストを用意
li = ["*"] * N

# 条件が矛盾している場合、1桁目がゼロ(N>1)の場合は-1を出力
# それ以外はリストにcを記録
for i in range(M):
  s, c = map(int, input().split())
  if li[s-1] != "*" and li[s-1] != c:
    print(-1)
    exit()
  if s == 1 and c == 0 and N > 1:
    print(-1)
    exit()
  li[s-1] = c

for i in range(N):
  if li[i] == "*": # リストに記録がない場合
    if i == 0 and N > 1: 
      li[i] = 1 # N>1で1桁目であれば1
    else:
      li[i] = 0 # N=1なら0
  print(li[i], end="")