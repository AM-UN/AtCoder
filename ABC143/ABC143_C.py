N = int(input())
S = input()

# 隣り合う文字が同じであれば1つとして扱う
ans = 1
for i in range(1, N):
  if S[i] != S[i-1]:
    ans += 1
print(ans)