# 入力
N = int(input())

name = ""
while N > 0:
    # zを出力できるよう事前に-1しておく
    N -= 1
    # 26で割った余りをa...zに変換して記録
    name += chr(97+(N % 26))
    # 次の桁に移動
    N //= 26
    
name = name[::-1]
print(name)