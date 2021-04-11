# 入力
N = input()
N_reverse = N[::-1]

# 0を0～10個まで左端に足して、逆から読んでも同じか判定 
for i in range(1, 10):
  N_add = "0"*i+N
  N_add_reverse = N_add[::-1]
  if N == N_reverse or N_add == N_add_reverse:
    print("Yes")
    exit()
print("No")