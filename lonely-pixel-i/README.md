# Leetcode: Lonely Pixel I     :BLOG:Medium:


---

Lonely Pixel I  

---

Similar Problems:  
-   [Lonely Pixel II](https://code.dennyzhang.com/lonely-pixel-ii)
-   [Set Matrix Zeroes](https://code.dennyzhang.com/set-matrix-zeroes)
-   [Tag: #array](https://code.dennyzhang.com/tag/array)

---

Given a picture consisting of black and white pixels, find the number of black lonely pixels.  

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.  

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.  

Example:  

    Input: 
    [['W', 'W', 'B'],
     ['W', 'B', 'W'],
     ['B', 'W', 'W']]
    
    Output: 3
    Explanation: All the three 'B's are black lonely pixels.

Note:  
The range of width and height of the input 2D array is [1,500].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/lonely-pixel-i)  

Credits To: [leetcode.com](https://leetcode.com/problems/lonely-pixel-i/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/lonely-pixel-i
    ## Basic Ideas:
    ##   Maintain two array, with initial value of 0
    ##     row_list: how many B for each row
    ##     col_list: how many B for each col
    ##
    ## Complexity: Time O(n*m), Space O(n+m)
    class Solution:
        def findLonelyPixel(self, picture):
            """
            :type picture: List[List[str]]
            :rtype: int
            """
            row_count = len(picture)
            if row_count == 0: return 0
            col_count = len(picture[0])
            row_list = [(0, None) for i in range(row_count)]
            col_list = [(0, None) for i in range(col_count)]
    
            for i in range(row_count):
                for j in range(col_count):
                    if picture[i][j] == 'B':
                        row_list[i] = (row_list[i][0]+1, j)
                        col_list[j] = (col_list[j][0]+1, i)
            res = 0
            for i in range(row_count):
                if row_list [i][0] != 1: continue
                j = row_list[i][1]
                if col_list[j] == (1, i): res += 1
            return res