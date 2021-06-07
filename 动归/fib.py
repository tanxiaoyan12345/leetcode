class Solution(object):
    # def fib(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n<1:
    #         return 0
    #     if n==1 or n==2:
    #         return 1
    #     dp = [0]*(n+1)
    #     dp[0] = 0
    #     dp[1] = dp[2] = 1
    #     for i in range(3,n+1):
    #         dp[i] = dp[i-1] + dp[i-2]
    #     return dp[n]

    #降空间复杂度
    def fib(self, n):
        if n<1:
            return 0
        if n==1 or n==2:
            return 1
        cur = 1
        pre = 1
        for i in range(3,n+1):
            res = cur + pre
            pre = cur
            cur = res
        return res


