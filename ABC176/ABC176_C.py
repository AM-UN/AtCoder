# 入力
N = int(input())
A = list(map(int, input().split()))

# 先頭の人と比較して、大きければその人を先頭とし、小さければその差を合計する
now = 0
count = 0
for i in range(N):
    if A[i] < now:
        count += now - A[i]
    else:
        now = A[i]
print(count)
