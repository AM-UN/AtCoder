# 入力
N = int(input())

# Aを固定してBが取りうる最大値を求める(CはA、Bが決まれば一意に求まる)
count = 0
for i in range(1, N):
    Bmax = (N-1)//i
    count += Bmax
print(count)
