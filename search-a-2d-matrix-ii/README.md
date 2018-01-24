# Leetcode: Search a 2D Matrix II     :BLOG:Medium:


---

Search a 2D Matrix  

---

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:  

Integers in each row are sorted in ascending from left to right.  
Integers in each column are sorted in ascending from top to bottom.  
For example,  

Consider the following matrix:  

    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]

Given target = 5, return true.  

Given target = 20, return false.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/search-a-2d-matrix-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/search-a-2d-matrix-ii
    class Solution(object):
        def searchMatrix(self, matrix, target):
            """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """