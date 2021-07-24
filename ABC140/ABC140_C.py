N = int(input())
B = list(map(int, input().split()))
A = 0
for i in range(1, N-1): # Aの先頭、一番後ろ以外の数
    A += min(B[i-1], B[i])
A += B[0]+B[N-2] # Bの最初と最後の項、インデックスだから1つ左にずれる
print(A)

# 紙に書く