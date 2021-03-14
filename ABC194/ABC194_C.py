# 入力
N = int(input())
A = list(map(int, input().split()))
 
# -200<=Ai<=200の範囲でAに含まれる数を記録
cnt = [0] * 401
for i in A:
    cnt[i+200] += 1
 
# i, jのそれぞれの要素の数に2つの要素の差の二乗をかける
ans = 0
for i in range(401):
    for j in range(i, 401):
        ans += cnt[i] * cnt[j] * (((j-200)-(i-200))**2)
print(ans)