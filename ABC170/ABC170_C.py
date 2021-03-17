# 入力
X, N = map(int, input().split())
p = list(map(int, input().split()))

# pに含まれていなくて、Xとの差の絶対値が小さいものを探していく
for i in range(X+1):
    if X - i not in p:
        print(X - i)
        exit()
    if X + i not in p:
        print(X + i)
        exit()