# Leetcode: Knight Probability in Chessboard     :BLOG:Medium:


---

Knight Probability in Chessboard  

---

Similar Problems:  
-   Tag: [#bfs](https://code.dennyzhang.com/tag/bfs), [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#possibilities](https://code.dennyzhang.com/tag/possibilities)

---

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).  

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.  

![img](//raw.githubusercontent.com/DennyZhang/images/master/code/knight.png)  

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.  

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.  

Example:  

    Input: 3, 2, 0, 0
    Output: 0.0625
    Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
    From each of those positions, there are also two moves that will keep the knight on the board.
    The total probability the knight stays on the board is 0.0625.

Note:  
-   N will be between 1 and 25.
-   K will be between 0 and 100.
-   The knight always initially starts on the board.

Note: The solution set must not contain duplicate subsets.  

    For example,
    If nums = [1,2,2], a solution is:
    
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/knight-probability-in-chessboard)  

Credits To: [leetcode.com](https://leetcode.com/problems/knight-probability-in-chessboard/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/knight-probability-in-chessboard
    ## Basic Ideas: BFS
    ##
    ##    If one element already in the queue. We add the possibility
    ##
    ## Complexity: Time O(k*n), Space O(n)
    class Solution:
        def knightProbability(self, N, K, r, c):
            """
            :type N: int
            :type K: int
            :type r: int
            :type c: int
            :rtype: float
            """
            import collections
            queue = collections.deque()
            queue.append((r, c))
            level = 0
            d = collections.defaultdict(lambda: 0)
            d[r*N+c] = 1
            while len(queue) != 0:
                level += 1
                # print(K, level, queue)
                if level > K: break
                for k in range(len(queue)):
                    (i, j) = queue.popleft()
                    possiblity = d[i*N+j]
                    d[i*N+j] = 0
                    # get the neighbors
                    for (ik, jk) in [(-1, 2), (1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                        i2, j2 = i+ik, j+jk
                        if i2<0 or i2>=N or j2<0 or j2>=N: continue
                        if d[i2*N+j2] == 0: queue.append((i2, j2))
                        d[i2*N+j2] += possiblity*(1/8)
            res = 0
            for (i, j) in queue: res += d[i*N+j]
            return res