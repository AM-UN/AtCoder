# 入力
N = int(input())

# 全探索をして、X > Aの中から最小のPであるものを出力(無ければ-1を出力)
price = []
for i in range(N):
    A, P, X = map(int,(input().split()))
    if X > A:
        price.append(P)
if price:
    print(min(price))
else:
    print(-1)

