# Leetcode: Pascal's Triangle II     :BLOG:Basic:


---

Pascal's Triangle II  

---

Similar Problems:  
-   [Leetcode: Pascal's Triangle](https://code.dennyzhang.com/pascals-triangle)

---

iven an index k, return the kth row of the Pascal's triangle.  

For example, given k = 3,  
Return [1,3,3,1].  

Note:  
Could you optimize your algorithm to use only O(k) extra space?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/pascals-triangle-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/pascals-triangle-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/pascals-triangle-ii
    class Solution(object):
        def getRow(self, rowIndex):
            """
            :type rowIndex: int
            :rtype: List[int]
            """
            if rowIndex == 0:
                return [1]
            l = [1] * (rowIndex + 1)
            for i in range(0, rowIndex+1):
                self.getNextRow(l, i)
    
            return l
    
        def getNextRow(self, num_list, currentRowCount):
            if currentRowCount == 0:
                num_list[0] = 1
                return
    
            if currentRowCount == 1:
                num_list[0] = 1
                num_list[1] = 1
                return
    
            # print("currentRowCount: %d" % (currentRowCount))
            for i in range(currentRowCount-1, 0, -1):
                num_list[i] = num_list[i] + num_list[i-1]