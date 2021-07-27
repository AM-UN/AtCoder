S = input()
ans = 0
op = len(S)-1
for i in range(2**op):
    s = S[0]
    for j in range(op):
        if (i>>j)&1:
            s += "+"
        s += S[j+1]
    if len(s) == len(S):
        ans += int(s)
    else:
        ans += sum([int(i) for i in s.split("+")])
print(ans)