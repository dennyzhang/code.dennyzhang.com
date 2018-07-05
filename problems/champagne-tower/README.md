# Leetcode: Champagne Tower     :BLOG:Medium:


---

Champagne Tower  

---

Similar Problems:  
-   [Reaching Points](https://code.dennyzhang.com/reaching-points)
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup (250ml) of champagne.  

Then, some champagne is poured in the first glass at the top.  When the top most glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has it's excess champagne fall on the floor.)  

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.  

![img](//raw.githubusercontent.com/DennyZhang/images/master/code/tower.png)  

Now after pouring some non-negative integer cups of champagne, return how full the j-th glass in the i-th row is (both i and j are 0 indexed.)  

Example 1:  

    Input: poured = 1, query_glass = 1, query_row = 1
    Output: 0.0
    Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:  

    Input: poured = 2, query_glass = 1, query_row = 1
    Output: 0.5
    Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

Note:  

-   poured will be in the range of [0, 10 ^ 9].
-   query\_glass and query\_row will be in the range of [0, 99].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/champagne-tower)  

Credits To: [leetcode.com](https://leetcode.com/problems/champagne-tower/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/champagne-tower
    ## Basic Ideas: Dynamic programming
    ##          grid[i][j] will evenly flow to grid[i+1][j] and grid[i+1][j+1]
    ##
    ## Complexity: Time O(1), Space O(1).
    ##             <= 100*100
    class Solution:
        def champagneTower(self, poured, query_row, query_glass):
            """
            :type poured: int
            :type query_row: int
            :type query_glass: int
            :rtype: float
            """
            dp = [0]*(query_glass+1)
            dp[0] = poured
            for i in range(1, query_row+1):
                l = [0]*(query_glass+1)
                for j in range(0, query_glass+1):
                    if j>=1 and dp[j-1] > 1:
                        l[j] += (dp[j-1]-1)/2
                    if dp[j]>1:
                        l[j] += (dp[j]-1)/2
                dp = l
            return min(dp[query_glass], 1)