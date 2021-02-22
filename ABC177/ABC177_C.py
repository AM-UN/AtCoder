# 入力
N = int(input())
A = list(map(int, input().split()))

# Aiを固定し、入力Aの累積和からAj以降の累積和を引いたものをAiとかけ、その総和を求める
mod = 10**9+7
sum_A = sum(A)
total = 0
for i in range(N-1):
    sum_A -= A[i]
    total += A[i]*sum_A
print(total % mod)

