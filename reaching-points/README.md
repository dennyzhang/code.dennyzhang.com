# Leetcode: Reaching Points     :BLOG:Medium:


---

Reaching Points  

---

Similar Problems:  
-   [Review: Recursive Problems](https://brain.dennyzhang.com/review-recursive), [Tag: #recursive](https://brain.dennyzhang.com/tag/recursive)

---

A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).  

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.  

    Examples:
    Input: sx = 1, sy = 1, tx = 3, ty = 5
    Output: True
    Explanation:
    One series of moves that transforms the starting point to the target is:
    (1, 1) -> (1, 2)
    (1, 2) -> (3, 2)
    (3, 2) -> (3, 5)
    
    Input: sx = 1, sy = 1, tx = 2, ty = 2
    Output: False
    
    Input: sx = 1, sy = 1, tx = 1, ty = 1
    Output: True

Note:  

sx, sy, tx, ty will all be integers in the range [1, 10^9].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reaching-points)  

Credits To: [leetcode.com](https://leetcode.com/problems/reaching-points/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/reaching-points
    ## Basic Ideas:
    ##   When tx > sx and ty > sy
    ##        we move from the target to the source by using mod functions
    ##
    ## Complexity:
    class Solution:
        def reachingPoints(self, sx, sy, tx, ty):
            """
            :type sx: int
            :type sy: int
            :type tx: int
            :type ty: int
            :rtype: bool
            """
            if tx<sx or ty<sy: return False
            if tx==sx: return (ty-sy) % tx == 0
            if ty==sy: return (tx-sx) % ty == 0
            if ty>tx:
                ty=ty%tx
            else:
                tx=tx%ty
            return self.reachingPoints(sx, sy, tx, ty)