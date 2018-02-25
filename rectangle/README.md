# LintCode: Rectangle     :BLOG:Medium:


---

Rectangle  

---

Similar Problems:  
-   Tag: [#rectangle](https://brain.dennyzhang.com/tag/rectangle)

---

Give a set, if you can find four points that make up a rectangle that is parallel to the coordinate axis and outputs YES or NO.  

 Notice  
The number of points in the set is less than 2000, and the coordinate range is [-10000000,10000000].  
Have you met this question in a real interview?  
Example  
Given set = [[0,0],[0,1],[1,1],[1,0]], return YES.  

Explanation:  
We can find four points that make up a rectangle which is parallel to the coordinate axis.  
Given set = [[0,0],[0,1],[1,1],[2,0]], return NO.  

Explanation:  
We can not find four points that meet the conditions  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/rectangle)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/rectangle/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/example
    #!/usr/bin/env python
    """
    class Point:
        def __init__( self, x=0, y=0):
            self.x = x
            self.y = y
    """
    class Solution:
        """
        @param pointSet: The point set
        @return: The answer
        """
        def rectangle(self, pointSet):
            ## Basic Ideas:
            ##   a, b, c
            ##   a*a+b*b=c*c
            ## Complexity: Time O(1), Space O(1)
            if len(pointSet) != 4: return 'NO'
            l = []
            for i in range(4):
                for j in range(4):
                    if i == j: continue
                    l.append(pow(pointSet[i].x-pointSet[j].x, 2)+pow(pointSet[i].y-pointSet[j].y, 2))
            mySet = set(l)
            count = len(mySet)
            # print(mySet)
            if count!=2 and count!=3: return 'NO'
            v1, v2 = min(mySet), max(mySet)
            c1, c2 = 0, 0
            for num in l:
                if num == v1: c1 += 1
                if num == v2: c2 += 1
            if len(l)%4 != 0 or c1%4 != 0 or c2%4 != 0: return 'NO'
            if count == 2:
                return 'YES' if v2 == 2*v1 else 'NO'
            else:
                v3 = None
                for num in mySet:
                    if num != v1 and num !=v2: v3 = num
                return 'YES' if v2 == v1+v3 else 'NO'