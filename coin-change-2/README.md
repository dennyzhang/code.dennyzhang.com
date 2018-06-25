
# Leetcode: Coin Change 2     :BLOG:Medium:

---

Coin Change 2  

---

Similar Problems:  

-   [Coin Change](https://code.dennyzhang.com/coin-change)
-   [Review: Knapsack Problems](https://code.dennyzhang.com/review-knapsack)
-   [Tag: #knapsack](https://code.dennyzhang.com/tag/knapsack)

---

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.  

Note: You can assume that  

-   0 <= amount <= 5000
-   1 <= coin <= 5000
-   the number of coins is less than 500
-   the answer is guaranteed to fit into signed 32-bit integer

Example 1:  

    Input: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1

Example 2:  

    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:  

    Input: amount = 10, coins = [10] 
    Output: 1

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/coin-change-2)  

Credits To: [leetcode.com](https://leetcode.com/problems/coin-change-2/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/coin-change-2
    class Solution(object):
        ## Basic Ideas: Dynamic programming
        ##   dp(i) = {coin1: count1, coin2: count2, coin3: count3, ...}
        ##           count_j is the combination with the maximum value as coin_j
        ##
        ## Complexity: Time O(k*n), Space O(n)
        def change(self, amount, coins):
    	"""
    	:type amount: int
    	:type coins: List[int]
    	:rtype: int
    	"""
    	if amount == 0: return 1
    	if len(coins) == 0: return 0
    	dp = [None]*(1+amount)
    	for i in range(0, amount+1): dp[i] = collections.defaultdict(lambda: 0)
    	for coin in coins: dp[0][coin] = 1
    	coins.sort()
    	for i in range(1, amount+1):
    	    for coin in coins:
    		if i<coin: break
    		v = i-coin
    		dp[i][coin] = dp[v][coin]
    
    	    dp[i][0] = 1
    	    for j in range(1, len(coins)):
    		dp[i][coins[j]] += dp[i][coins[j-1]]
    
    	return dp[amount][coins[-1]]

