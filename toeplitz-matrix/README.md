# Leetcode: Toeplitz Matrix     :BLOG:Basic:


---

Toeplitz Matrix  

---

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.  

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.  

Example 1:  

    Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    Output: True
    Explanation:
    1234
    5123
    9512
    
    In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.

Example 2:  

    Input: matrix = [[1,2],[2,2]]
    Output: False
    Explanation:
    The diagonal "[1, 2]" has different elements.

Note:  

1.  matrix will be a 2D array of integers.
2.  matrix will have a number of rows and columns in range [1, 20].
3.  matrix[i][j] will be integers in range [0, 99].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/toeplitz-matrix)  

Credits To: [leetcode.com](https://leetcode.com/problems/toeplitz-matrix/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/toeplitz-matrix
    ## Basic Ideas: Check all m[i][j] with m[i+1][j+1]
    ##
    ##            (0,0)  (1,0)  (2,0)  (3,0)
    ##              1     2       3     4
    ##              5     1       2     3
    ##              9     5       1     2
    ##            (0,2)  (1,2)  (2,2)  (3,2)
    ##
    ## Complexity: Time O(m*n), Space O(1)
    class Solution(object):
        def isToeplitzMatrix(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: bool
            """
            row_count = len(matrix)
            if row_count == 0: return True
            col_count = len(matrix[0])
            for i in xrange(row_count-1):
                for j in xrange(col_count-1):
                    if matrix[i][j] != matrix[i+1][j+1]:
                        return False
            return True