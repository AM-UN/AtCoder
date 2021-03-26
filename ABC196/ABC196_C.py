# 入力
N = input()

N_length = len(N)

# 数列の桁数が偶数ならば
if N_length % 2 == 0:
    # 数列を前半と後半に分ける
    front = N[:(N_length//2)]
    back = N[(N_length//2):]
    # 前半よりも後半の数の方が大きければ前半の数を出力、そうでなければ後半の数を出力
    if int(front) <= int(back):
        print(front)
    else:
        print(int(front)-1)
# 数列の桁数が偶数でないならば
else:
    # 数列の桁数が1なら0、そうでないなら桁数を一つ下げ偶数にし、
    # 前半と後半で文字列が等しくなる最大の数を出力
    if N_length == 1:
        print(0)
    else:
        print("9"*(N_length//2))
