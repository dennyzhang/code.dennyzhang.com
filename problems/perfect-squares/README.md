
# Leetcode: Perfect Squares     :BLOG:Medium:

---

Perfect Squares  

---

Similar Problems:  

-   [Review: sqrt Problems](https://code.dennyzhang.com/review-sqrt)
-   [Review: Classic Code Problems](https://code.dennyzhang.com/review-classic)
-   Tag: [#classic](https://code.dennyzhang.com/tag/classic), [sqrt](https://code.dennyzhang.com/tag/sqrt)

---

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, &#x2026;) which sum to n.  

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/perfect-squares)  

Credits To: [leetcode.com](https://leetcode.com/problems/perfect-squares/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/perfect-squares
    ## Basic Ideas: BFS. Find the mininum steps
    ##              Get a list of square numbers as the candidate to explore
    ##
    ## Complexity: Time O(n*n), Space O(n)
    class Solution:
        def numSquares(self, n):
    	"""
    	:type n: int
    	:rtype: int
    	"""
    	square_list = []
    	i = 1
    	while i*i <= n:
    	    if i*i == n: return 1
    	    square_list.append(i*i)
    	    i += 1
    
    	level = 0
    	queue = set([n])
    
    	while len(queue) != 0:
    	    level += 1
    	    # use set, since we will have duplicate numbers to check
    	    s = set([])
    	    for num in queue:
    		for square in square_list:
    		    new_val = num - square
    		    if new_val == 0: return level
    		    # The follow values won't fix
    		    if new_val < 0: break
    		    # next candidate
    		    s.add(new_val)
    	    queue = s
    
    	# we shouldn't go to this line
    	return None
    
    # s = Solution()
    # print(s.numSquares(12)) # 3
    # print(s.numSquares(7168)) # 4
    # print(s.numSquares(1103))
    # print(s.numSquares(5756))
    # print(s.numSquares(6255))

