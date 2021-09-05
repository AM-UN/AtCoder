X, Y = map(int,input().split())

ans = 0
# XがYを超えるまで2倍し、倍にした回数を出力
while X <= Y:
  X = X*2
  ans += 1
    
print(ans)