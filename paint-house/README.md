# Leetcode: Paint House     :BLOG:Medium:


---

Paint House  

---

Similar Problems:  
-   [Paint Fence](https://brain.dennyzhang.com/paint-fence)
-   Tag: [#dynamicprogramming](https://brain.dennyzhang.com/tag/dynamicprogramming)

---

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.  

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.  

    For example, costs[0][0] is the cost of painting house 0 with color red; 
    costs[1][2] is the cost of painting house 1 with color green, and so on...
    Find the minimum cost to paint all houses.

Note:  
All costs are positive integers.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/paint-house)  

Credits To: [leetcode.com](https://leetcode.com/problems/paint-house/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/paint-house
    ## Basic Ideas: Dyanmic programming
    ##     For house after house1, it can only have 3 possilities.
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def minCost(self, costs):
            """
            :type costs: List[List[int]]
            :rtype: int
            """
            length = len(costs)
            if length == 0: return 0
    
            dp = [None]*3
    
            # caculate house I
            dp = costs[0]
    
            # caculate the following house
            for i in range(1, length):
                l = [None]*3
                for j in range(0, 3):
                    l[j] = costs[i][j] + min(dp[(j+1)%3], dp[(j+2)%3])
                dp = l
            return min(dp)