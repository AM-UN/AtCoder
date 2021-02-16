# 入力
N = int(input())
count = 0

# 入力を10進数と8進数の文字列に直して、それぞれに7が含まれてるか判定
for i in range(1, N+1):
    if not "7" in str(i) and not  "7" in oct(i):
        count += 1
print(count)