# 入力
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

# 同じマスの場合
if (r1, c1) == (r2, c2):
    count = 0

# 条件1を満たすよう動かした場合
elif r1 + c1 == r2 + c2:
    count = 1

# 条件2を満たすよう動かした場合
elif r1 - c1 == r2 - c2:
    count = 1

# 条件3を満たすよう動かした場合
elif abs((r1 - r2))+abs((c1 - c2))<=3:
    count = 1

# 1手目で条件1(2)を、2手目で条件2(1)を満たすよう動かした場合
elif (r1+r2+c1+c2) % 2 == 0:
    count = 2

# 1手目で条件1を、2手目で条件3を満たすよう動かした場合
elif abs((r1 + c1)-(r2 + c2))<=3:
    count = 2

# 1手目で条件2を、2手目で条件3を満たすよう動かした場合
elif abs((r1 - c1)-(r2 - c2))<=3:
    count = 2

# 1手目、2手目それぞれで条件3を満たすよう動かした場合
elif abs((r1 - r2))+abs((c1 - c2))<=6:
    count = 2

# それ以外
else:
    count = 3

print(count)