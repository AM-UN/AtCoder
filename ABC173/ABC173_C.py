# 入力
H, W, K = map(int, input().split())
squares = [list(input()) for i in range(H)]

# それぞれの行と列に関して、赤く塗るか塗らないかをbit全探索
ans = 0
for i in range(2**H):
    for j in range(2**W):
        count = 0
        for k in range(H):        
            for l in range(W):
                # マスが赤く塗られてなくて、もともと黒いマスならカウント
                if (i>>k)&1 == 0 and (j>>l)&1 == 0 and squares[k][l]=="#":
                    count += 1
        # カウントした数とKを比較して、同じならカウント
        if count == K:
            ans += 1  
print(ans)
