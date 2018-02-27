# Leetcode: Coin Change     :BLOG:Basic:


---

Coin Change  

---

Similar Problems:  
-   [Perfect Squares](https://brain.dennyzhang.com/perfect-squares)
-   [Coin Change 2](https://brain.dennyzhang.com/coin-change-2)
-   [Review: Knapsack Problems](https://brain.dennyzhang.com/review-knapsack), [Tag: #knapsack](https://brain.dennyzhang.com/tag/knapsack)
-   [Review: Classic Code Problems](https://brain.dennyzhang.com/review-classic), [Tag: #classic](https://brain.dennyzhang.com/tag/classic)

---

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.  

Example 1:  

    coins = [1, 2, 5], amount = 11
    return 3 (11 = 5 + 5 + 1)

Example 2:  

    coins = [2], amount = 3
    return -1.

Note:  
You may assume that you have an infinite number of each kind of coin.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/coin-change)  

Credits To: [leetcode.com](https://leetcode.com/problems/coin-change/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/coin-change
    class Solution(object):
        ## Basic Ideas: Dynamic Programming
        ##
        ##    dp(i) = min(dp(i), dp[i-coin[j]]+1)
        ## Complexity: Time O(n) Space O(n)
        def coinChange(self, coins, amount):
            """
            :type coins: List[int]
            :type amount: int
            :rtype: int
            """
            if amount == 0: return 0
            import sys
            coins.sort()
            dp = [0] + [sys.maxsize]*(amount)
    
            for i in range(1, amount+1):
                for coin in coins:
                    if coin > i: break
                    if dp[i-coin] != sys.maxsize:
                        dp[i] = min(dp[i], dp[i-coin]+1)
    
            return dp[amount] if dp[amount] != sys.maxsize else -1 
    
        ## Basic Ideas: BFS
        ##
        ## Complexity: Time O(n) Space O(n)
        def coinChange_v1(self, coins, amount):
            """
            :type coins: List[int]
            :type amount: int
            :rtype: int
            """
            if amount == 0: return 0
            coins.sort()
            d = {}
            queue = collections.deque()
            queue.append(0)
            level = 0
            while len(queue) != 0:
                level += 1
                for k in range(len(queue)):
                    num = queue.popleft()
                    for coin in coins:
                        v = coin + num
                        if v > amount: break
                        if v == amount: return level
                        # avoid duplicate
                        if v not in d:
                            d[v] = level
                            queue.append(v)
            return -1