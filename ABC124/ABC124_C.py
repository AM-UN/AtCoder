S = input()
N = len(S)

# 偶数、奇数の番号のタイルに分ける
even = S[0::2]
odd = S[1::2]

# 隣り合う2つのタイルが異なるパターンは"10101…"か"01010…"の二つのみ
# Sがそれらのパターンになるのに何回タイルの色を変えるか
ptn_0 = N-(even.count("0")+odd.count("1"))
ptn_1 = N-(even.count("1")+odd.count("0"))

ans = min(ptn_0,ptn_1)
print(ans)