A = input()
n = len(A)-1 # +,-,+ の長さ
for i in range(2**n): 
    sum = int(A[0]) # sumと7が一致するか後で判定(出力はしない)
    ans = A[0]      # Trueの場合、出力の一部
    for j in range(n): 
        if (i >> j) & 1:
            sum += int(A[j+1])
            ans += "+"
        else:
            sum -= int(A[j+1])
            ans += "-"
        ans += A[j+1]
    if sum == 7:
        print(ans+"=7")
        exit()