def solution(n):
    answer = 0
    
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(1,n+1):
        for j in range(i):
            dp[i]+=dp[j]*dp[i-j-1]
    
    answer=dp[n]
    
    return answer