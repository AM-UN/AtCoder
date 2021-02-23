# 入力
X, K, D = map(int, input().split())

x = abs(X)
# 歩ける範囲がXより小さい場合、その差を出力
if x >= K*D:
    print(x-K*D)
# 歩ける範囲がXより大きい場合
else:
    mod = x % D
    # 原点から最も近くまでいき、残りの歩数が偶数だったらその座標を出力
    if (K-(x//D)) % 2 == 0:    
        print(mod)
    # 原点から最も近くまでいき、残りの歩数が奇数だったらもう1歩先までいった座標を出力
    else:
        print(D-mod)
