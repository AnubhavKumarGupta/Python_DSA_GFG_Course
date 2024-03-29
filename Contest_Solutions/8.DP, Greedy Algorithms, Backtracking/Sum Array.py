#User function Template for python3
class Solution:
    def solve(self, N, a):
        # code here
        if N == 0:
            return []
        if N == 1:
            return [a[0]]
        
        dp = [0]*N
        dp[0] = a[0]
        dp[1] = max(a[0],a[1])
        
        for i in range(2,N):
            dp[i] = max(dp[i-1], dp[i-2] + a[i])

        result = []
        for i in range(N):
            result.append(dp[i])
        return result
        
        
        