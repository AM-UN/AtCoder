H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for i in range(1, H):
    for j in range(1, W):
        count = 0
        if S[i-1][j-1]=="#":
            count += 1
        if S[i-1][j]=="#":
            count += 1
        if S[i][j-1]=="#":
            count += 1
        if S[i][j]=="#":
            count += 1
        if count % 2 == 1:
            ans += 1
print(ans)