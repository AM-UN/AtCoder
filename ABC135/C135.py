# 入力
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 貪欲法(各時点で最良のものを選択)
count = 0
for i in range(N):
    if A[i]>=B[i]:
        count+=B[i]
    else:
        count+=A[i]
        B[i]-=A[i]
        if A[i+1]>=B[i]:
            count+=B[i]
            A[i+1]-=B[i]
        else:
            count+=A[i+1]
            A[i+1]=0
print(count)
