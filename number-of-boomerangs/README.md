# Leetcode: Number of Boomerangs     :BLOG:Medium:


---

Number of Boomerangs  

---

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).  

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).  

    Example:
    Input:
    [[0,0],[1,0],[2,0]]
    
    Output:
    2
    
    Explanation:
    The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/number-of-boomerangs)  

Credits To: [leetcode.com](https://leetcode.com/problems/number-of-boomerangs/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/number-of-boomerangs
    class Solution(object):
        def numberOfBoomerangs(self, points):
            """
            :type points: List[List[int]]
            :rtype: int
            """