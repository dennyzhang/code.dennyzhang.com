
# Leetcode: Spiral Matrix     :BLOG:Medium:

---

Spiral Matrix  

---

Similar Problems:  

-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails)

---

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.  

    For example,
    Given the following matrix:
    
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    You should return [1,2,3,6,9,8,7,4,5].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/spiral-matrix)  

Credits To: [leetcode.com](https://leetcode.com/problems/spiral-matrix/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/spiral-matrix
    ## Basic Ideas:
    ##            The visit is a loop with four directions: right, down, left, up
    ##            Two counters: num1(how many items for right and left)
    ##                          num2 (how many items for down and up)
    ##            num1, num2 = column_count, row_count - 1
    ##               right     down     left     up
    ##               num1--   num2--   num1--   num2--
    ##               num1--   num2--   num1--   num2--
    ##            Quit if num1 == 0 or num2 == 0
    ## Complexity: Time O(m*n), Space O(1)
    class Solution(object):
        def spiralOrder(self, matrix):
    	"""
    	:type matrix: List[List[int]]
    	:rtype: List[int]
    	"""
    	row_count = len(matrix)
    	if row_count == 0:
    	    return []
    	res = []
    	column_count = len(matrix[0])
    	num1, num2 = column_count, row_count - 1
    	direction_list = 'rdlu'
    	direction_index = 0
    	i, j = 0, 0
    	while True:
    	    direction = direction_list[direction_index]
    	    # print("num1: %d, num2: %d, direction: %s" % (num1, num2, direction))
    	    if direction in 'rl':
    		direction_count = num1
    		num1 -= 1
    	    else:
    		direction_count = num2
    		num2 -= 1
    	    if direction_count == 0:
    		break
    	    for k in xrange(direction_count):
    		# print("i: %d, j:%d" % (i, j))
    		res.append(matrix[i][j])
    		if k == direction_count - 1:
    		    # move to next direction
    		    if direction == 'r':
    			i += 1
    		    if direction == 'd':
    			j -= 1
    		    if direction == 'l':
    			i -= 1
    		    if direction == 'u':
    			j += 1
    		else:
    		    # move to next element
    		    if direction == 'r':
    			j += 1
    		    if direction == 'd':
    			i += 1
    		    if direction == 'l':
    			j -= 1
    		    if direction == 'u':
    			i -= 1
    	    direction_index = (direction_index+1) % 4
    	return res

