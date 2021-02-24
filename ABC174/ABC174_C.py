# 入力
K = int(input())

# Kで割って余りが出なければ終了、出たら1つ桁を増やして同じことを繰り返す(上限はK桁)
now = 7
for i in range(K):
    MOD = now % K
    if MOD == 0:
        print(i+1)
        exit()
    now = MOD*10+7
print(-1)
