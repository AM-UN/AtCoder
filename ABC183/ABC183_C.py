# itertoolsモジュールのpermutation関数をインポート
from itertools import permutations

# 入力
N, K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]

# 都市1を除いた経路の順列
route_list = [i for i in range(2, N+1)]
route_permutations = permutations(route_list)

# 全ての経路を全探索して、移動時間がKと同じになる回数を求める
count = 0
for i in route_permutations:
    sum = 0
    city = 0
    for j in range(N-1):        
        sum += T[city][i[j]-1]
        city = i[j]-1           
    sum += T[city][0]
    
    if sum == K:
        count += 1
print(count)