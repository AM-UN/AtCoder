from math import gcd
A, B = map(int, input().split())

# 最小公倍数を求める
ans = A * B // gcd(A, B)
print(ans)