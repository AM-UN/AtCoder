# mathモジュールの導入
import math

# 入力
R, X, Y = map(int, input().split())

# 点(X,Y)までの距離
distance = (X**2+Y**2)**(1/2)

# ちょうどRしか移動できない場合、点(X,Y)まで何歩かかるか出力
ans = math.ceil(distance/R)
if R > distance:
  ans = ans+1
print(ans)