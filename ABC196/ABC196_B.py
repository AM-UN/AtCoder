# 入力
N = input()
 
# "."がNに含まれていれば、整数部分だけを取得する
if "." in N:
    a = N.find(".")
    print(N[:a])
else:
    print(N)