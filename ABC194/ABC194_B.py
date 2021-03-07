# 入力
N = int(input())
A = []
B = []
 
for i in range(N):
    a, b = map(int,(input().split()))
    A.append(a)
    B.append(b)
 
# 仕事A, Bに割り当てる従業員を全探索し、仕事を終わらす最小の時間を求める
ans = 100000
for i in range(N):
    for j in range(N):
        # 仕事A, Bを同じ従業員が行う場合、2つの仕事にかかった合計の時間
        if i == j:
            ans = min(ans, A[i] + B[j])
        # 仕事A, Bをそれぞれ違う従業員が行う場合、仕事にかかる時間が大きい方
        else:
            ans = min(ans, max(A[i], B[j]))
        
print(ans)
