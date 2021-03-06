# itertoolsモジュールのaccumulate関数をインポート
from itertools import accumulate
# bisectモジュールのbisect_right関数をインポート
from bisect import bisect_right

# 入力
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# AとBの累積和
A_acc = [0] + list(accumulate(A))
B_acc = [0] + list(accumulate(B))

# AからA_sum冊取った場合、Kに達するまで残り何冊Bから取れるか2分探索法を用いて求める
j = 0
ans = 0
for A_sum in range(N+1):
    if A_acc[A_sum] <= K:
        rem = K - A_acc[A_sum]
        B_sum = bisect_right(B_acc, rem)
        ans = max(ans, A_sum + B_sum -1)
print(ans)
