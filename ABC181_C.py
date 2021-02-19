# itertoolsモジュールのcombinations関数をインポート
from itertools import combinations

# 入力
N = int(input())
num = [list(map(int, input().split())) for i in range(N)]

# 入力から3つの点を選び、同一直線上にあればYes、なければNoを出力
count = 0
for i in combinations(num, 3):
    dot = list(i)
    if (dot[1][1]-dot[0][1])*(dot[2][0]-dot[1][0]) == (dot[2][1]-dot[1][1])*(dot[1][0]-dot[0][0]):
        print("Yes")
        exit()
print("No")
