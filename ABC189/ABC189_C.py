# 入力
N = int(input())
A = list(map(int, input().split()))

# lを固定し、r番目までの最小のみかんの数、その範囲でのみかんの合計、最大の合計を求める
orange_max = 0
for l in range(N):
    orange = A[l]
    for r in range(l, N):
        orange = min(orange, A[r])
        total = orange*(r-l+1)
        orange_max = max(total, orange_max)
print(orange_max)