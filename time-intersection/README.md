# LintCode: Time Intersection     :BLOG:Medium:


---

Time Intersection  

---

Similar Problems:  
-   Tag: [#interval](https://brain.dennyzhang.com/tag/interval)

---

Give two users' ordered online time series, and each section records the user's login time point x and offline time point y. Find out the time periods when both users are online at the same time, and output in ascending order.  

 Notice  
We guarantee that the length of online time series meet 1 <= len <= 1e6.  
For a user's online time series, any two of its sections do not intersect.  
Have you met this question in a real interview?  
Example  
Given seqA = [[1,2],[5,100]], seqB = , return [[1,2],[5,6]].  

Explanation:  
In these two time periods [1,2],[5,6], both users are online at the same time.  
Given seqA = [[1,2],[10,15]], seqB = [[3,5],[7,9]], return [].  

Explanation:  
There is no time period, both users are online at the same time.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/time-intersection)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/time-intersection/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/time-intersection
    """
    class Point:
        def __init__( self, x=0, y=0):
            self.x = x
            self.y = y
    """
    class Solution:
        """
        @param seqA: The seqA
        @param seqB: The seqB
        @return: The answer
        """
        def timeIntersection(self, seqA, seqB):
            ## Basic Idea: Binary search
            ## Complexity: Time O(n*log(n)), Space O(n)
            if len(seqA) >=0 and len(seqB)>=0 and seqA[0].x > seqB[0].x:
                return self.timeIntersection(seqB, seqA)
    
            start_list = []
            for seq in seqA: start_list.append(seq.x)
    
            res = []
            for seq2 in seqB:
                x, y = seq2.x, seq2.y
                # TODO: further improvement. Left doesn't need to be 0 each time
                # binary search
                left, right = 0, len(start_list)-1
                while left<=right:
                    mid = left + int((right-left)/2)
                    v = start_list[mid]
                    if v == x:
                        break
                    if v<x:
                        left = mid + 1
                    else:
                        right = mid - 1
    
                i = mid if left<=right else max(right, 0)
                while i < len(start_list) and seqA[i].x <= y:
                    # check whether 2 interval overlapping
                    x2, y2 = max(seqA[i].x, x), min(seqA[i].y, y)
                    if x2<=y2: res.append(Point(x2, y2))
                    i += 1
            return res