# 入力
N = int(input())

# a**b <= N となるaを全探索(a**2 >= Nのa以降は探索しなくていい)
s = set()
search_range = int(N**(0.5))
for i in range(2, search_range+1):
    now = i ** 2
    while now <= N:
        s.add(now)
        now *= i
print(N-len(s))

