# mathモジュールをインポート
import math

# 入力を受け取って切断可能な箇所の数に直す
L = int(input())
l = L-1

# 切断可能な個所から11箇所分割する組み合わせを求める
ans = math.factorial(l)//(math.factorial(11)*math.factorial(l-11))
print(ans)