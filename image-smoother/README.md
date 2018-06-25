# Leetcode: Image Smoother     :BLOG:Amusing:


---

Image Smoother  

---

Similar Problems:  
-   [Tag: #matrixtraverse](https://code.dennyzhang.com/tag/matrixtraverse)

---

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.  

    Example 1:
    Input:
    [[1,1,1],
     [1,0,1],
     [1,1,1]]
    Output:
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
    Explanation:
    For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
    For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
    For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:  
1.  The value in the given matrix is in the range of [0, 255].
2.  The length and width of the given matrix are in the range of [1, 150].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/image-smoother)  

Credits To: [leetcode.com](https://leetcode.com/problems/image-smoother/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/image-smoother
    ## Basic Ideas: The main point is how to write clean code.
    ##
    ##
    ## Complexity: Time O(n*m), Space O(1) Here we don't count the result list
    class Solution(object):
        def imageSmoother(self, M):
            """
            :type M: List[List[int]]
            :rtype: List[List[int]]
            """
            self.row_count = len(M)
            if self.row_count == 0: return None
            self.col_count = len(M[0])
            # How to initialize 2D matrix for the result
            res = [None]*self.row_count
            for i in xrange(self.row_count):
                res[i] = [None]*self.col_count
    
            for i in xrange(self.row_count):
                for j in xrange(self.col_count):
                    count, sum_val = 0, 0
                    for k in [-1, 0, 1]:
                        (sum_val, count) = self.addValue(M, i-1, j+k, sum_val, count)
                        (sum_val, count) = self.addValue(M, i, j+k, sum_val, count)
                        (sum_val, count) = self.addValue(M, i+1, j+k, sum_val, count)
                    # print("i: %d, j:%d, sum_val: %d, count: %d" % (i, j, sum_val, count))
                    # python itself will roud down
                    res[i][j] = sum_val/count
            return res
    
        def addValue(self, M, i, j, sum_val, count):
            if i>=0 and i<self.row_count and j>=0 and j<self.col_count:
                return (sum_val+M[i][j], count+1)
            else:
                return (sum_val, count)
    
    # s = Solution()
    # print s.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])
    # [[4,4,5],[5,6,6],[8,9,9],[11,12,12],[13,13,14]]