# 関数を定義
def f(x):
  # g_1(x) (各桁の数字を大きい順に並び変えた数)
  g1 = int(''.join(sorted(str(x))[::-1]))
  # g_2(x) (各桁の数字を小さい順に並び変えた数)
  g2 = int(''.join(sorted(str(x))))
  # g_1 - g_2を返す
  return g1 - g2

# 入力
N, K = map(int, input().split())

# a_Kを出力
for i in range(K):
  N = f(N)
print(N)

