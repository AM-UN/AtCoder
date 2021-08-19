import math
K = int(input())

ans = 0
# 1からKの値まで変化する3つの値のそれぞれの最大公約数の和を求める
for i in range(1, K+1):
  for j in range(1, K+1):
    gcd = math.gcd(i, j)
    for k in range(1, K+1):
      ans += math.gcd(gcd, k)
print(ans)