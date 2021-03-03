# bisectモジュールのインポート、入力
import bisect
N = int(input())
# 祭壇の上部、中部、下部のパーツを並び変えて取得
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

# 中部を固定して、A>B、B<CとなるAとCの組み合わせを求める
ans = 0
for i in B:
    idx_A = bisect.bisect_left(A, i)
    idx_C = bisect.bisect_right(C, i)
    ans += idx_A * (N-idx_C)

print(ans)
