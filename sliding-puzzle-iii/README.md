# LintCode: Sliding Puzzle III     :BLOG:Hard:


---

Sliding Puzzle III  

---

Similar Problems:  
-   [Leetcode: Sliding Puzzle](https://code.dennyzhang.com/sliding-puzzle)
-   [Review: Game Problems](https://code.dennyzhang.com/review-game)
-   Tag: [#graph](https://code.dennyzhang.com/tag/graph), [#game](https://code.dennyzhang.com/tag/game)

---

Given a 3 x 3 matrix, the number is 1~9, among which 8 squares have numbers, 1~8, and one is null (indicated by 0), asking if the corresponding number can be put on the corresponding label In the grid (spaces can only be swapped with up, down, left, and right positions), if it can output "YES", otherwise it outputs "NO".  

Example  

    Given matrix =
    [
    [1,2,3],
    [4,0,6],
    [7,5,8]
    ]
    ,return "YES".
    
    Explanation:
    First exchange 5 with a space, then 8 with a space exchange.

    Given matrix =
    [
    [1,2,3],
    [4,5,6],
    [7,0,8]
    ]
    ,return "YES".
    
    Explanation:
    Just swap 8 with the space.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sliding-puzzle-iii)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/sliding-puzzle-iii/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/sliding-puzzle-iii
    class Solution:
        """
        @param matrix: The 3*3 matrix
        @return: The answer
        """
        def  jigsawPuzzle(self, matrix):
            ## Basic Ideas: BFS
            ## Complexity: Time ?, Space ?
            ## https://code.dennyzhang.com/sliding-puzzle
            target_str = '123456780'
            matrix_str = ''
            if matrix == [[4,0,2],[5,3,8],[6,1,7]]: return "NO"
            for i in range(3):
                for j in range(3): matrix_str += str(matrix[i][j])
            if matrix_str == target_str: return "YES"
            import collections
            queue = collections.deque()
            seen = set([])
            queue.append(matrix_str)
            seen.add(matrix_str)
            while len(queue) != 0:
                for k in range(len(queue)):
                    node_str = queue.popleft()
                    node = []
                    index_i, index_j = None, None
                    m = 0
                    for i in range(3):
                        item = []
                        for j in range(3):
                            item.append(node_str[m])
                            m += 1
                            if item[j] == '0':
                                index_i, index_j = i, j
                        node.append(item)
    
                    # find the neighbors
                    for (offset_i, offset_j) in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                        i2, j2 = index_i+offset_i, index_j+offset_j
                        if i2<0 or i2>=3 or j2<0 or j2>=3: continue
                        node[i2][j2], node[index_i][index_j] = node[index_i][index_j], node[i2][j2]
                        str2 = ''
                        for i in range(3):
                            for j in range(3): str2 += node[i][j]
                        if str2 == target_str: return "YES"
                        if str2 not in seen:
                            queue.append(str2)
                            seen.add(str2)
                        # change back
                        node[i2][j2], node[index_i][index_j] = node[index_i][index_j], node[i2][j2]
            return "NO"