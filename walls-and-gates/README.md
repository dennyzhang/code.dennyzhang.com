# Leetcode: Walls and Gates     :BLOG:Medium:


---

Walls and Gates  

---

Similar Problems:  
-   [Shortest Distance from All Buildings](https://brain.dennyzhang.com/shortest-distance-from-all-buildings)
-   [01 Matrix](https://brain.dennyzhang.com/01-matrix)
-   [Review: BFS Problems](https://brain.dennyzhang.com/review-bfs)

---

You are given a m x n 2D grid initialized with these three possible values.  

1.  -1 - A wall or an obstacle.
2.  0 - A gate.
3.  INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.  

For example, given the 2D grid:  

    INF  -1  0  INF
    INF INF INF  -1
    INF  -1 INF  -1
      0  -1 INF INF

After running your function, the 2D grid should be:  

    3  -1   0   1
    2   2   1  -1
    1  -1   2  -1
    0  -1   3   4

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/walls-and-gates)  

Credits To: [leetcode.com](https://leetcode.com/problems/walls-and-gates/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/walls-and-gates
    ## Basic Ideas: BFS
    ##      For each 0, and configure the values to the level number
    ##      If the neighbors is 0 or value equals current level, skip them
    ##
    ## Complexity: Time O(?), Space O(n*n)
    class Solution:
        def wallsAndGates(self, rooms):
            """
            :type rooms: List[List[int]]
            :rtype: void Do not return anything, modify rooms in-place instead.
            """
            import collections
            row_count = len(rooms)
            if row_count == 0: return
            col_count = len(rooms[0])
            for i in range(row_count):
                for j in range(col_count):
                    if rooms[i][j] == 0:
                        queue = collections.deque([(i, j)])
                        level = 0
                        while len(queue) != 0:
                            level += 1
                            for k in range(len(queue)):
                                (i1, j1) = queue.popleft()
                                # get the neighbors
                                for (ik, jk) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                    i2, j2 = i1+ik,j1+jk
                                    if i2<0 or i2>=row_count \
                                        or j2<0 or j2>=col_count:
                                            continue
                                    if rooms[i2][j2] <= level: continue
                                    rooms[i2][j2] = level
                                    queue.append((i2, j2))