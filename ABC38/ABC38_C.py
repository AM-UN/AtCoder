# 入力
N = int(input())
a = list(map(int, input().split()))

# 尺取り法によって、単調増加となる(l, r)の数を求める
r, count = 0, 0
for l in range(N):
    while r+1 < N and a[r] < a[r+1]:       
        r += 1
    count += r-l+1
    if l == r:
        r += 1
print(count)
    
