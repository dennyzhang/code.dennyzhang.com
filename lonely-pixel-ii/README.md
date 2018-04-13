# Leetcode: Lonely Pixel II     :BLOG:Medium:


---

Lonely Pixel II  

---

Similar Problems:  
-   [Lonely Pixel I](https://code.dennyzhang.com/lonely-pixel-i)
-   [Tag: #array](https://code.dennyzhang.com/tag/array)

---

Given a picture consisting of black and white pixels, and a positive integer N, find the number of black pixels located at some specific row R and column C that align with all the following rules:  

Row R and column C both contain exactly N black pixels.  
For all rows that have a black pixel at column C, they should be exactly the same as row R  
The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.  

Example:  

    Input:                                            
    [['W', 'B', 'W', 'B', 'B', 'W'],    
     ['W', 'B', 'W', 'B', 'B', 'W'],    
     ['W', 'B', 'W', 'B', 'B', 'W'],    
     ['W', 'W', 'B', 'W', 'B', 'W']] 
    
    N = 3
    Output: 6
    Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
            0    1    2    3    4    5         column index                                            
    0    [['W', 'B', 'W', 'B', 'B', 'W'],    
    1     ['W', 'B', 'W', 'B', 'B', 'W'],    
    2     ['W', 'B', 'W', 'B', 'B', 'W'],    
    3     ['W', 'W', 'B', 'W', 'B', 'W']]    
    row index
    
    Take 'B' at row R = 0 and column C = 1 as an example:
    Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels. 
    Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. They are exactly the same as row R = 0.

Note:  
The range of width and height of the input 2D array is [1,200].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/lonely-pixel-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/lonely-pixel-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/lonely-pixel-ii
    ## Basic Ideas:
    ##    Two array
    ## Complexity: Time O(n*m), Space O(n+m)
    class Solution:
        def findBlackPixel(self, picture, N):
            """
            :type picture: List[List[str]]
            :type N: int
            :rtype: int
            """
            row_count = len(picture)
            if row_count == 0: return 0
            col_count = len(picture[0])
            row_list = [0 for i in range(row_count)]
            col_list = [0 for i in range(col_count)]
    
            for i in range(row_count):
                for j in range(col_count):
                    if picture[i][j] == 'B':
                        col_list[j] += 1
                        row_list[i] += 1
            res = 0
            for i in range(row_count):
                for j in range(col_count):
                    if picture[i][j] == 'B' and col_list[j] == N and row_list[i] == N:
                        res += 1
            return res