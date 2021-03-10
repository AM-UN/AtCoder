# 入力
N = input()

length = len(N)
del_count = 20

# bit全探索で消す最小の桁数を求める
for i in range(2**length):
    char = ""
    for j in range(length):
        if (i>>j) & 1:
            char += N[j]
    if char == "":
        continue
    if int(char) % 3 == 0:
        del_count = min(del_count, length-len(char))
print(del_count if not del_count == 20 else -1)