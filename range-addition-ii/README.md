# Leetcode: Range Addition II     :BLOG:Medium:


---

Range Addition II  

---

Similar Problems:  
-   [Review: Math Problems,](https://brain.dennyzhang.com/review-math) Tag: [math](https://brain.dennyzhang.com/tag/math)

---

Given an m \* n matrix M initialized with all 0's and several update operations.  

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.  

You need to count and return the number of maximum integers in the matrix after performing all the operations.  

Example 1:  

    Input: 
    m = 3, n = 3
    operations = [[2,2],[3,3]]
    Output: 4
    Explanation: 
    Initially, M = 
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
    
    After performing [2,2], M = 
    [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 0]]
    
    After performing [3,3], M = 
    [[2, 2, 1],
     [2, 2, 1],
     [1, 1, 1]]
    
    So the maximum integer in M is 2, and there are four of it in M. So return 4.

Note:  
1.  The range of m and n is [1,40000].
2.  The range of a is [1,m], and the range of b is [1,n].
3.  The range of operations size won't exceed 10,000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/range-addition-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/range-addition-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/range-addition-ii
    ## Basic Ideas: The biggest number will happen in the left-corner
    ##             min(ops_i) * min(ops_j)
    ##
    ## Complexity: Time O(len(ops)) Space O(1)
    class Solution(object):
        def maxCount(self, m, n, ops):
            """
            :type m: int
            :type n: int
            :type ops: List[List[int]]
            :rtype: int
            """
            min_i, min_j = m, n
            for (i, j) in ops:
                min_i = min(i, min_i)
                min_j = min(j, min_j)
            return min_i*min_j