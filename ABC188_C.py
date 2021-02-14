# 入力
N = int(input())
A = list(map(int, input().split()))

# トーナメント表の半分の山で一番強い人同士を戦わせて準優勝を決める
second_place = min(max(A[:2**(N-1)]), max(A[2**(N-1):]))
print(A.index(second_place)+1)