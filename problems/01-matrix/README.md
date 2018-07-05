
# Leetcode: 01 Matrix     :BLOG:Amusing:

---

01 Matrix  

---

Similar Problems:  

-   Tag: [#graph](https://code.dennyzhang.com/tag/graph)

---

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.  

The distance between two adjacent cells is 1.  
Example 1:  

    Input:
    
    0 0 0
    0 1 0
    0 0 0
    Output:
    0 0 0
    0 1 0
    0 0 0

Example 2:  

    Input:
    
    0 0 0
    0 1 0
    1 1 1
    Output:
    0 0 0
    0 1 0
    1 2 1

Note:  

1.  The number of elements of the given matrix will not exceed 10,000.
2.  There are at least one 0 in the given matrix.
3.  The cells are adjacent in only four directions: up, down, left and right.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/problems/01-matrix)  

Credits To: [leetcode.com](https://leetcode.com/problems/01-matrix/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/01-matrix
    ## Basic Ideas:
    ##        There are two types of 1: Adjacent nodes have 0; don't have
    ##
    ##        BFS. 
    ##          Use type1 as layer 1. Mark it as -1. Then keep exploring the next level
    ##          How to avoiding check one element twice?
    ##              We have marked type1 as -1. So any processed positions will not be 1 any more.
    ##
    ## Complexity: Time O(m*n), Space O(1)
    import sys
    class Solution(object):
        def updateMatrix(self, matrix):
    	"""
    	:type matrix: List[List[int]]
    	:rtype: List[List[int]]
    	"""
    	self.row_count = len(matrix)
    	if self.row_count == 0: return matrix
    	self.col_count = len(matrix[0])
    	queue = []
    	# mark elements which are 1 and also near 0
    	for i in xrange(self.row_count):
    	    for j in xrange(self.col_count):
    		if matrix[i][j] == 1 and self.adjacentHasValue(matrix, i, j, 0):
    		    matrix[i][j] = -1
    		    queue.append((i, j))
    
    	level = 2
    	while len(queue) != 0:
    	    for k in xrange(len(queue)):
    		(i, j) = queue[0]
    		del queue[0]
    		# find neighbors
    		for (offset_i, offset_j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    		    next_i, next_j = i+offset_i, j+offset_j
    		    if next_i < 0 or next_i >= self.row_count or \
    			next_j <0 or next_j >= self.col_count:
    			    continue
    		    if matrix[next_i][next_j] == 1:
    			matrix[next_i][next_j] = level
    			queue.append((next_i, next_j))
    	    level += 1
    
    	# change -1 back to 1
    	for i in xrange(self.row_count):
    	    for j in xrange(self.col_count):
    		if matrix[i][j] == -1: matrix[i][j] = 1
    	return matrix
    
        def adjacentHasValue(self, matrix, i, j, value):
    	if i!=0 and matrix[i-1][j] == value: return True
    	if i!=self.row_count-1 and matrix[i+1][j] == value: return True
    	if j!=0 and matrix[i][j-1] == value: return True
    	if j!=self.col_count-1 and matrix[i][j+1] == value: return True
    	return False
    
    # s = Solution()
    # matrix = [[1, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0]]
    # s.updateMatrix(matrix)
    # print matrix

