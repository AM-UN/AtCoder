# 入力
N, M = map(int, input().split())
term = [[int(i) for i in input().split()] for j in range(M)]
K = int(input())
dish = [[int(i) for i in input().split()] for j in range(K)]

maximum = 0
# bit全探索で皿Ciと皿Diのどちらにボールが置かれているか求める
for i in range(2**K):
    ball = [0]*N
    for j in range(K):
        if (i>>j)&1:
            ball[dish[j][0]-1] += 1
        else:
            ball[dish[j][1]-1] += 1

    # 最大で条件を何個満たしてるか求める
    count = 0
    for i in range(M):
        if ball[term[i][0]-1] >= 1 and ball[term[i][1]-1] >= 1:
            count += 1
    if count > maximum:
        maximum = count
print(maximum)
