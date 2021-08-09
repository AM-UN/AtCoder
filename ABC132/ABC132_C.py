N = int(input())
d = sorted(list(map(int, input().split())))

# ARC用の問題とABC用の問題が同じ数になるようなKを求める
ABC = d[N//2-1]
ARC = d[N//2]
K = ARC-ABC

print(K)