# Leetcode: Spiral Matrix II     :BLOG:Medium:


---

Spiral Matrix II  

---

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.  

    For example,
    Given n = 3,
    
    You should return the following matrix:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/spiral-matrix-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/spiral-matrix-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/spiral-matrix-ii
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
        def generateMatrix(self, n):
            """
            :type n: int
            :rtype: List[List[int]]
            """
            if n <= 0:
                return []
            res = []
            for i in xrange(n):
                res.append([None]*n)
    
            num1, num2 = n, n - 1
            direction_list = 'rdlu'
            i, j = 0, 0
            v, direction_index = 1, 0
            while True:
                direction = direction_list[direction_index]
                if direction in 'rl':
                    direction_count = num1
                    num1 -= 1
                else:
                    direction_count = num2
                    num2 -= 1
                if direction_count == 0:
                    break
                # visit line
                for k in xrange(direction_count):
                    res[i][j] = v
                    v += 1
                    if k != direction_count - 1:
                        if direction == 'r':
                            j += 1
                        if direction == 'd':
                            i += 1
                        if direction == 'l':
                            j -= 1
                        if direction == 'u':
                            i -= 1
                    else:
                        if direction == 'r':
                            i += 1
                        if direction == 'd':
                            j -= 1
                        if direction == 'l':
                            i -= 1
                        if direction == 'u':
                            j += 1
                direction_index = (direction_index+1) % 4
            return res
    
    # s = Solution()
    # print s.generateMatrix(3)