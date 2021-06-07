
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #备忘录递归法
        # memo = dict()
        # def dp(n):
        #     if n in memo: 
        #         return memo[n]
        #     if n == 0:
        #         return 0
        #     if n<0:
        #         return -1
        #     res = float('INF')
        #     for coin in coins:
        #         subproblem = dp(n-coin)
        #         if subproblem == -1:
        #             continue
        #         res = min(res, subproblem+1)
        #     memo[n] = res if res!=float('INF') else -1
        #     return memo[n] #提前用备忘录算好每个状态对应的值
        # return dp(amount)

        #dp数组迭代解法
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount]!=amount+1 else -1


