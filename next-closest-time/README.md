# Leetcode: Next Closest Time     :BLOG:Medium:


---

Next Closest Time  

---

Similar Problems:  

-   [Tag: #manydetails](https://brain.dennyzhang.com/tag/manydetails)

---

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.  

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.  

Example 1:  

    Input: "19:34"
    Output: "19:39"
    Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:  

    Input: "23:59"
    Output: "22:22"
    Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/next-closest-time)  

Credits To: [leetcode.com](https://leetcode.com/problems/next-closest-time/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/next-closest-time
    ## Basic Ideas: Only pow(4, 4) combinations
    ##      Get all of them, and rule out the invalid onces
    ##      Convert the time string to seconds
    ##      Compare the absolute diff with rotated enforced
    ##
    ## Assumption: "11:11" -> "11:11"
    ## Complexity:
    class Solution:
        def nextClosestTime(self, time):
            """
            :type time: str
            :rtype: str
            """
            import sys
            ch_set = set(time)
            ch_set.remove(':')
            if len(ch_set) == 1: return time
    
            l = [""]
            for i in range(4):
                l2 = 
                for ch in ch_set:
                    for item in l:
                        if i == 1:
                            l2.append("%s%s:" % (item, ch))
                        else:
                            l2.append("%s%s" % (item, ch))
                l = l2
    
            minutes = self.getMinutes(time)
            min_diff, index  = sys.maxsize, None
            total_minutes = 24*60
            for i in range(len(l)):
                t = l[i]
                # check whether t is valid
                if int(t[0])*10+int(t[1]) >= 24: continue
                if int(t[3])*10+int(t[4]) >= 60: continue
    
                diff = (self.getMinutes(t)-minutes+total_minutes) % total_minutes
                if diff == 0: continue
    
                if min_diff > diff:
                    min_diff, index = diff, i
    
            return l[index]
    
        def getMinutes(self, time):
            return (int(time[0])*10 + int(time[1]))*60+(int(time[3])*10 + int(time[4]))