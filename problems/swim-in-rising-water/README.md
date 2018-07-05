
# Leetcode: Swim in Rising Water     :BLOG:Amusing:

---

Swim in Rising Water  

---

Similar Problems:  

-   Tag: [#graph](https://code.dennyzhang.com/category/graph)

---

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).  

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.  

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?  

Example 1:  

    Input: [[0,2],[1,3]]
    Output: 3
    Explanation:
    At time 0, you are in grid location (0, 0).
    You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
    
    You cannot reach point (1, 1) until time 3.
    When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:  

    Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16
    Explanation:
     0  1  2  3  4
    24 23 22 21  5
    12 13 14 15 16
    11 17 18 19 20
    10  9  8  7  6
    
    The final route is marked in bold.
    We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Note:  

1.  2 <= N <= 50.
2.  grid[i][j] is a permutation of [0, &#x2026;, N\*N - 1].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/swim-in-rising-water)  

Credits To: [leetcode.com](https://leetcode.com/problems/swim-in-rising-water/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/swim-in-rising-water
    class Solution:
        ## Basic Ideas: BFS + heap
        ##     The water flows with nearly no delay, if it permits
        ##     Always explore with the slowest
        ##
        ## Complexity: Time O(n*n*log(n)), Space O(n*n)
        def swimInWater(self, grid):
    	"""
    	:type grid: List[List[int]]
    	:rtype: int
    	"""
    	row_count = len(grid)
    	if row_count <= 1: return 0
    
    	import heapq
    	visited, q = set([]), []
    	heapq.heapify(q)
    	heapq.heappush(q, (grid[0][0], 0, 0))
    	visited.add((0, 0))
    	res = 0
    	while len(q) != 0:
    	    (v, i, j) = heapq.heappop(q)
    	    # explore with the current minimum candidate
    	    res = max(res, v)
    	    for ik, jk in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    		i2, j2 = i+ik, j+jk
    		if i2<0 or i2>=row_count or j2<0 or j2>=row_count:
    		    continue
    		if (i2, j2) in visited: continue
    		if (i2, j2) == (row_count-1, row_count-1):
    		    return max(res, grid[i2][j2])
    		heapq.heappush(q, (grid[i2][j2], i2, j2))
    		visited.add((i2, j2))
    	return res

