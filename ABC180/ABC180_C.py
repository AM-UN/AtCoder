# 入力
N = int(input())

# √N以下の約数は√N以上の約数と対になっているため、√Nの範囲で全探索する
ans = []
num = int(N**(1/2))
for i in range(1, num+1):
    if N % i == 0:
        ans.append(i)
        pair = N//i
        if not pair == i:
            ans.append(pair)
ans.sort()
print(*ans, sep="\n")