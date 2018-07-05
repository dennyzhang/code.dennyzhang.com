# Leetcode: Minimum Time Difference     :BLOG:Basic:


---

Minimum Time Difference  

---

Similar Problems:  
-   Tag: [#basic](https://code.dennyzhang.com/category/basic)

---

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.  
Example 1:  

    Input: ["23:59","00:00"]
    Output: 1

Note:  
1.  The number of time points in the given list is at least 2 and won't exceed 20000.
2.  The input time is legal and ranges from 00:00 to 23:59.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/minimum-time-difference)  

Credits To: [leetcode.com](https://leetcode.com/problems/minimum-time-difference/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/minimum-time-difference
    ## Basic Ideas: Convert string to integer. 
    ##              Sort it. Then get difference with rotation enforced
    ##
    ## Complexity: Time O(1), Space O(1). There are only 60*24 possibilities.
    class Solution:
        def findMinDifference(self, timePoints):
            """
            :type timePoints: List[str]
            :rtype: int
            """
            l = []
            setPoints = set(timePoints)
            # duplicate entries
            if len(setPoints) != len(timePoints):
                return 0
            for timepoint in setPoints:
                [hour, minute] = timepoint.split(':')
                l.append(int(hour)*60+int(minute))
    
            l.sort()
            min_val = (l[0]+24*60-l[-1]) % (24*60)
            for i in range(1, len(l)):
                min_val = min(min_val, l[i] - l[i-1])
            return min_val