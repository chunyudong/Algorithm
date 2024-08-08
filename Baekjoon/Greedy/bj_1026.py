N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B_s = sorted(B)
A_s = sorted(A)
#print(B_s , A_s)

ans = 0
for i in range(N):
    ans += B_s[i] * A_s[-i-1]
print(ans)