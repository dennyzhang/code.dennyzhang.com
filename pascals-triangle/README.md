# Leetcode: Pascal Triangle     :BLOG:Basic:


---

Given numRows, generate the first numRows of Pascal's triangle.  

---

Given numRows, generate the first numRows of Pascal's triangle.  

    For example, given numRows = 5,
    Return
    
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]

Blog link: <http://brain.dennyzhang.com/pascals-triangle>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def generate(self, numRows):
            """
            :type numRows: int
            :rtype: List[List[int]]
            """
            l = []
            if numRows == 1:
                l.append([1])
    
            if numRows >= 2:
                l.append([1])
                l.append([1, 1])
    
            j = 3
            for i in range(2, numRows):
                item = []
                item.append(1)
                for k in range(1, j-1):
                    item.append(l[i-1][k-1] + l[i-1][k])
                item.append(1)
                l.append(item)
                j += 1 
    
            return l