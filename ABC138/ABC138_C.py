N = int(input())
v = list(map(int, input().split()))
v.sort()

# vのうち小さい値2つを(x+y)/2とし1つとする、それを繰り返す
# 最後に残った1つの値を出力
for i in range(N-1):
  v[i+1] = (v[i] + v[i+1]) / 2 
  
ans = v[N-1]
print(ans)