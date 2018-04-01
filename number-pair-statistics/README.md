# Leetcode: Number Pair Statistics     :BLOG:Basic:


---

Number Pair Statistics  

---

Similar Problems:  
-   [Tag: #inspiring](https://brain.dennyzhang.com/tag/inspiring)

---

Given a List <Point> p, find the number of (i,j) pairs that satisfy both p[i].x + p[j].x and p[i].y + p[j].y(i < j) can be divisible by 2.  

 Notice  
The length of given list len <= 10000.  

Example  

    Given p = [[1,2],[3,4],[5,6]], return 3.
    
    Explanation:
    
    p[0],p[1],p[2] Pairwise Covering, the sum of their x and y can be divided by 2

    Given p = [[0,3],[1,1],[3,4],[5,6]], return 1.
    
    Explanation:
    Only when p [2] and p [3] are combined, their sum of x and y can be divided by two.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/number-pair-statistics)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/number-pair-statistics/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/number-pair-statistics
    class Solution:
        """
        @param p: the point List
        @return: the numbers of pairs which meet the requirements
        """
        def pairNumbers(self, p):
            ## Basic Ideas: Types of odd and event
            ## Complexity: Time O(n), Space O(1)
            # odd_odd odd_even, even_odd, even_even
            l = [0]*4
            for point in p:
                x, y = point.x, point.y
                if x%2 == 1 and y%2 == 1: l[0] += 1
                if x%2 == 1 and y%2 == 0: l[1] += 1
                if x%2 == 0 and y%2 == 1: l[2] += 1
                if x%2 == 0 and y%2 == 0: l[3] += 1
            res = 0
            for i in range(4):
                if l[i] >= 2: res += int(l[i]*(l[i]-1)/2)
            return res