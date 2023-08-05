import sys
 
 
def cozum(A, K, M):
    if K == 0 or M == 0 or A == []:
        return 0
 
    if K == 1:
        return max(A)
 
    dp = list(A[:1-K])
    for i in range(1, len(dp)):
        dp[i] = max(dp[i-1], dp[i])
    for k in range(2, K+1):
        i = k % M
        dp0 = [0 for _ in dp]
        for j in range(len(dp)):
            if j == 0:
                dp0[j] = dp[j] + (A[k-1+j] * i)
            else:
                dp0[j] = max(dp[j] + (A[k-1+j] * i), dp0[j-1])
        dp = dp0
    return max(dp)
 
 
def main():
    N, K, M = (int(i) for i in sys.stdin.readline().split())
    A = [int(i) for i in sys.stdin.readline().split()]
    print(cozum(A, K, M))
 
 
if __name__ == '__main__':
    main()