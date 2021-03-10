# 入力
N = int(input())
a = []
b = []

# 入力された文字列の先頭に!があるかないかで配列分ける
for _ in range(N):
    S = input()
    if S[0] == "!":
        a.append(S[1:])
    else:   
        b.append(S)

# それぞれの配列に共通の文字列があるか求める
ans = list(set(a)&set(b))
if ans:
    print(ans[0])
else:
    print("satisfiable")