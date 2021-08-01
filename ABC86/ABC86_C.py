N = int(input())

t0 = x0 = y0 = 0
for i in range(N):
  t, x, y = map(int, input().split())
  # 移動に可能な時間
  dt = t - t0
  # 移動した距離(移動にかかった時間)
  distance = abs(x-x0) + abs(y-y0)
  
  if dt < distance or t % 2 != (x + y) % 2:
    print("No")
    exit()
  else: 
    # 入力値を記録
    t0 = t
    x0 = x
    y0 = y

print("Yes")